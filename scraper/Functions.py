from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from config_getter import get_config
DB_CONFIGS = get_config("db.json")

BUCKET_NAME = DB_CONFIGS["BUCKET"]
INFLUX_URL = DB_CONFIGS["URL"]
INFLUX_PASSWORD = DB_CONFIGS["INFLUX_PASSWORD"]
INFLUX_USERNAME = DB_CONFIGS["INFLUX_USERNAME"]

def Get_SetupDriver(url, headless=True):
    """
    Sets up and return Chrome WebDriver for the given url.
    
    Args:
        url (string): URL Chrome WebDriver should open
        headless (bool, optional): Opens URL with or without opening a browser. Defaults to True.

    Returns:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Chrome WebDriver
    """
    options = Options()
    if headless:
        # WebDriver opens Chrome with browser
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def open_InfluxDB_UI():
    # """ 
    # Shows the price course of the Amazon Product by opening the InfluxDB GUI automatically.

    # """
    # browser = Get_SetupDriver(INFLUX_URL, headless=False)

    # # Logging in in InfluxDB GUI
    # time.sleep(1)
    # username_el = browser.find_element_by_id("login")
    # username_el.send_keys(INFLUX_USERNAME)
    # password_el = browser.find_element_by_id("password")
    # password_el.send_keys(INFLUX_PASSWORD)
    # time.sleep(1)
    # submit_btn_el = browser.find_element_by_id("submit-login")
    # submit_btn_el.click()

    # # open Data Explorer
    # time.sleep(2)
    # browser.get(
    #     f"http://localhost:8086/orgs/5fc0694877b42f65/data-explorer?bucket={BUCKET_NAME}")

    # # set Filter to product_id
    # time.sleep(1.5)
    # element = browser.find_element_by_xpath(
    #     "//*[@id=\"cf-app-wrapper\"]/div[3]/div[3]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/button/span[1]")
    # element.click()
    # element = element.find_element_by_xpath(
    #     "//*[@id=\"cf-app-wrapper\"]/div[3]/div[3]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[4]/div")
    # element.click()

    # # select ASIN
    # time.sleep(1.5)
    # element = browser.find_element_by_xpath(
    #     "//*[@id=\"cf-app-wrapper\"]/div[3]/div[3]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]")
    # element.click()

    # # select on Price
    # time.sleep(1.5)
    # element = browser.find_element_by_xpath(
    #     "//*[@id=\"cf-app-wrapper\"]/div[3]/div[3]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/div[3]/div/div/div/div/div/div[2]/div[2]")
    # element.click()

    # # click on Submit
    # time.sleep(1.5)
    # element = browser.find_element_by_xpath(
    #     "//*[@id=\"cf-app-wrapper\"]/div[3]/div[3]/div/div/div/div/div[3]/div/div/div/div[1]/div[2]/button[3]/span")
    # element.click()
    print(f"http://localhost:8086/orgs/5fc0694877b42f65/data-explorer?bucket={BUCKET_NAME}")
