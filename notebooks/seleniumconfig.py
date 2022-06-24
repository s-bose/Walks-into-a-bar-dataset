import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
load_dotenv()



def get_driver(headless: bool = True) -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--incognito')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if headless:
        options.add_argument('--headless')

    service: Service = Service(os.environ.get('CHROMEDRIVER_PATH'))

    driver: WebDriver = webdriver.Chrome(service=service, options=options)
    driver.delete_all_cookies()

    return driver


if __name__ == "__main__":
    driver = get_driver()
    driver.implicitly_wait(1)
    driver.quit()
    