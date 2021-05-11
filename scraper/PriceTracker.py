from AmazonProduct import *
import crud
from datetime import datetime
from influxdb_client import Point
from config_getter import get_config
DB_CONFIGS = get_config("db.json")

BUCKET_NAME = DB_CONFIGS["BUCKET"]


class Scraper:
    """
    A class to manage the Scraping of a Amazon Product

    Args:
        amazon_product (AmazonProduct): Amazon Product to be scraped
        wish_price (float): Wish Price for the Amazon Product
        notify_email (str): Email which will be notified when wish price is reached

    Attributes:
        __product (AmazonProduct): Scraped Amazon Product
        __wish_price (float): Wish Price for the Amazon Product
        __tag_key (str): Tag key for InfluxDB Bucket "product_id"
        __tag_value (str): Tag value for IfnluxDB Bucket which is the ASIN
        __notify_email (str): Email which will be notified when wish price is reached

    """
    def __init__(self, amazon_product, wish_price, notify_email):
        """
        __init__ method sets up all attributes of class and creates InfluxDB Bucket if needed

        Args:
            product_url (string): URL of Amazon Product
        """
        self.__product = amazon_product
        self.__wish_price = float(wish_price)
        self.__tag_key = "product_id"
        self.__tag_value = str(self.__product.product_id)
        self.__notify_email = notify_email

        # create bucket only if it's not existing
        crud.create_bucket(BUCKET_NAME)

    def check_wish_price_satisfied(self, current_price):
        """
        Checks whether the current price equals less or is 1 more expensive than the wish price.

        Args:
            current_price (float): current price

        Returns:
            True||False: Boolean whether wish price is satisfied or not
        """
        
        if current_price <= self.__wish_price and current_price+1 >= self.__wish_price:
            return True
        return False

    def scraping_loop(self):
        """
        Loop which does the scraping process for the Amazon Product until wish price is reached.

        """
        flag = True
        openedInfluxDB_UI = False
        while flag:
            # get current info
            current_price = self.__product.get_price()
            current_rating = self.__product.get_review_starsRate()
            current_reviewNumber = self.__product.get_numberOfReviews()
            self.print_current_info()

            # prepare Points
            points = []
            if current_price:
                points.append(Point("measurements").tag(self.__tag_key, self.__tag_value).field("Price", float(current_price))) 
            if current_rating:
                points.append(Point("measurements").tag(
                self.__tag_key, self.__tag_value).field("Rating", float(current_rating)))
            if current_reviewNumber:
                points.append(Point("measurements").tag(self.__tag_key,
                                                     self.__tag_value).field("Number_of_Reviews", float(current_reviewNumber)))
            
            # write Points in Bucket
            crud.write_points(points=points, bucket_name=BUCKET_NAME)

            if openedInfluxDB_UI == False:
                open_InfluxDB_UI()
                openedInfluxDB_UI = True
            
            # notify user ?
            if self.check_wish_price_satisfied(current_price):
                flag = False
                self.notify_consumer()
            time.sleep(5)

    def print_current_info(self):
        """
        Prints formatted information about price, rating and number of reviews at the time.

        """
        # get current info
        now = datetime.now()
        currency = self.__product.get_currency()
        current_price = self.__product.get_price()
        current_rating = self.__product.get_review_starsRate()
        current_reviewNumber = self.__product.get_numberOfReviews()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # print current info
        print(f"[{dt_string}]")
        print("Current Information for Product:")
        print(f"    Price is: {current_price}{currency}")
        print(f"    Rating is: {current_rating}/5")
        print(f"    Number of Reviews is: {current_reviewNumber}")

    def notify_consumer(self):
        """
        Notifies the user by an email when the price of the scraped Amazon Product reaches the wish price.

        Returns:
            None: When sending the email failed
        """

        # prepare notification email
        title = self.__product.title
        price = str(self.__product.get_price())
        currency = CURRENCY[self.__product.get_currency()]
        link = self.__product.productURL
        message = f"""
        Hey you,

        it's me your Friendly Scraper! 
        I've keeping an eye on {title}.
        Well don't miss this special offer and get it for {price} {currency}.
        Buy it at {link} .

        Sincerely, 
        Your Friendly Scraper
        """

        # send notification email to given email
        try:
            
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(SCRAPER_EMAIL, SCRAPER_ACC_PASSWORD)
            server.sendmail(SCRAPER_EMAIL, self.__notify_email, message)
            server.quit()
        except Exception as e:
            print(e)
            print(f"Failed to send E-Mail")
            return None

