from config_getter import get_config
import re
from Functions import *

WEB_CONFIGS = get_config("amazon_web.json")

WEB_TITLE_ID = WEB_CONFIGS["WEB_TITLE_ID"]
WEB_REVIEWS_ID = WEB_CONFIGS["WEB_REVIEWS_ID"]


def product_id_legit(product_id: str):
    if product_id:
        if product_id != "product" and product_id.count("-")==0:
            return True
    return False

class AmazonProduct:
    """
    A class to represent a Amazon Product

    Args:
        product_url (str): URL of Amazon Product

    Attributes:
        __driver (selenium.webdriver.chrome.webdriver.WebDriver): Chrome WebDriver
        productURL (str): URL of Amazon Product
        product.id (str): ASIN

    """
    def __init__(self, product_url):
        """
        __init__ method sets up the Chrome WebDriver, title and ASIN of the Amazon Product

        Args:
            product_url (string): URL of Amazon Product
        """
        self.productURL = product_url
        self.__driver = Get_SetupDriver(self.productURL)
        self.set_title()
        self.set_product_id()

    def set_title(self):
        """[summary]
        Sets title of Amazon Product

        Returns:
            None: When setting title fails
        """
        try:
            self.title = self.__driver.find_element_by_id(WEB_TITLE_ID).text
        except Exception as e:
            print(str(e))
            print(
                f"Failed to set title of the product - {self.__driver.current_url}")
            return None

    def set_product_id(self):
        """
        Sets ASIN of Amazon Product

        Returns:
            None: When setting product ID fails
        """
        
        # all possible Amazon Product URLs
        regex_options = [
            r"https://www.amazon.[\w-]+/[\w-]+/product/(?P<product_id>[\w-]+)",
            r"https://www.amazon.[\w-]+/[\w-]+/[\w-]+/(?P<product_id>[\w-]+)",
            r"https://www.amazon.[\w-]+/[\w-]+/(?P<product_id>[\w-]+)",
            r"https://www.amazon.[\w-]+/(?P<slug>[\w-]+)/dp/(?P<product_id>[\w-]+)"
        ]
        try:
            # get product id out of URL
            for regex_case in regex_options:
                product_id = None
                regex = re.compile(regex_case)
                match = regex.match(self.productURL)
                if match:
                    try:
                        product_id = match['product_id']
                        if product_id_legit(product_id):
                            self.product_id = product_id
                            return
                    except:
                        pass
            self.product_id = None
        except Exception as e:
            print(e)
            print(
                f"Failed to set ASIN of the product - {self.__driver.current_url}")
            return None

    def get_price(self):
        """
        Gets current price of Amazon Product

        Returns:
            price (float): price of Amazon Product
            None: When getting the price fails
        """
        try:
            # seperate price from currency
            price_info = self.__driver.find_element_by_id(WEB_CONFIGS["WEB_PRICE_ID"]).text
            price = float(price_info.split()[0].replace(',', '.'))
            return price
        except Exception as e:
            print(e)
            print(
                f"Failed to get price of the product - {self.__driver.current_url}")
            return None

    def get_currency(self):
        """
        Gets currency of price of Amazon Product

        Returns:
            currency (str): currency of price of Amazon Product
        """
        # seperate currency from price
        price_info = self.__driver.find_element_by_id(WEB_CONFIGS["WEB_PRICE_ID"]).text
        currency = price_info.split()[1]
        return currency

    def get_review_starsRate(self):
        """
        Gets star rating of Amazon Product

        Returns:
            rating (float): rating out of 5
            None: When getting the rating fails
        """
        try:
            # format star rating into float
            rating = self.__driver.find_element_by_id(
                WEB_REVIEWS_ID).find_element_by_class_name(WEB_CONFIGS["WEB_RATING_CLASS"]).text
            rating = re.findall(r"[-+]?\d*\,\d+|\d+", rating)
            rating = float(rating[0].replace(',', '.'))
            return rating
        except Exception as e:
            print(e)
            print(
                f"Failed to get ASIN of the product - {self.__driver.current_url}")
            return None

    def get_numberOfReviews(self):
        """
        Gets number of reviews of Amazon Product

        Returns:
            numberOfReviews: number of Reviews of Amazon Product
        """
        try:
            # format number of reviews into int
            numberOfReview = self.__driver.find_element_by_id(
                WEB_CONFIGS["WEB_NUMBER_REVIEWS_ID"]).text
            numberOfReview = re.findall(r"[-+]?\d*\.\d+|\d+", numberOfReview)
            numberOfReview = int(numberOfReview[0].replace('.', ''))
            return numberOfReview
        except Exception as e:
            print(e)
            print(
                f"Failed to get ASIN of the product - {self.__driver.current_url}")
            return None
