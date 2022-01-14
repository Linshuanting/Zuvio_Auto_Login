from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

LOGIN_URL = 'https://irs.zuvio.com.tw/'


class Log_in():
    def __init__(self, account, url, driver):
        self.url = url
        self.account = account
        self.driver = driver

    def login(self):
        self.driver.get(self.url)

        email = self.driver.find_element_by_id("email")
        passwd = self.driver.find_element_by_id("password")

        email.send_keys(self.account["uid"])
        passwd.send_keys(self.account["passwd"])
        passwd.submit()

        time.sleep(3)
        return self.driver

    def get_driver(self):
        return self.driver
    


class OpenDriver():
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(
            "D:\code\python\DataBase_Final\chromedriver.exe", chrome_options=options)

        return None

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver


if __name__ == '__main__':
    driver = OpenDriver()
    log = Log_in(account, LOGIN_URL, driver.get_driver())
    driver = log.login()
