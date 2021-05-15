from PriceTracker import *


def main(url: str, wish_price: float, notify_email: str, openInfluxDB_GUI: bool):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Message:")
    print(f"    I will scrape the product from {url}")
    print(f"    I will notify your Email: {notify_email}, when the products costs {wish_price} €|$|£ or less!")
    print("Initialize Scraping Infos about the Product...")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    product = AmazonProduct(url)
    scraper = PriceTracker(amazon_product=product, wish_price=wish_price,
                      notify_email=notify_email, openInfluxDB_GUI=openInfluxDB_GUI)
    scraper.scraping_loop()

if __name__ == "__main__":
    url = str(input("Please paste URL of Amazon Product: "))
    wish_price = float(input("Please enter desired price [xx.xx]: "))
    notify_email = str(input("Please enter your email: "))
    openInfluxDB_GUI = bool(input("Open InfluxDB GUI to see Price Chart [True||False]: "))
    main(url, wish_price, notify_email, openInfluxDB_GUI)
