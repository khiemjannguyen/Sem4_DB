from PriceTracker import *

def main (url: str, wish_price: float, notify_email: str):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Message:")
    print(f"    I will scrape the product from {url}")
    print(f"    I will notify your Email: {notify_email}, when the products costs {wish_price} €|$|£ or less!")
    print("Initialize Scraping Infos about the Product...")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("URL FOR INFLUX")
    open_InfluxDB_UI()
    product = AmazonProduct(url)
    scraper = Scraper(amazon_product=product, wish_price=wish_price, notify_email=notify_email)
    scraper.scraping_loop()

if __name__ == "__main__":
    url = str(input("Please paste an Amazon Product Url: "))
    wish_price = float(input("Please give Wish Price [xx.xx]: "))
    notify_email = str(input("Please give me your E-Mail: "))
    main(url, wish_price, notify_email)
