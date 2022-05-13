import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
load_dotenv()

CHROMEDRIVER_PATH: str = '/home/bose/Projects/barjoke/chromedriver'

def get_driver(headless: bool = True) -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--incognito')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if headless:
        options.add_argument('--headless')

    service: Service = Service(CHROMEDRIVER_PATH)

    driver: WebDriver = webdriver.Chrome(service=service, options=options)
    driver.delete_all_cookies()

    return driver