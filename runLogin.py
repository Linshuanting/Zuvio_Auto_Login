from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import Login
import RollCall


LOGIN_URL = 'https://irs.zuvio.com.tw/'


class RunLogin():
    def __init__(self):
        return None

    def run(self, name, account, amount):
        driver = Login.OpenDriver()
        log = Login.Log_in(account, LOGIN_URL, driver.get_driver())
        driver = log.login()
        rc = RollCall.RC(driver)
        rc.toCourses(name, amount)
        driver = rc.get_driver()


if __name__ == '__main__':
    app = RunLogin()
    app.run("生命教育", account, 10)
    
