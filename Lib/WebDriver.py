'''
Created on Mar 15, 2020

@author: DELL
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import  ElementNotVisibleException
import time


class clsWebDriver:
    def ChromeDriver(self):
        WebOptions = webdriver.ChromeOptions()
        WebOptions.add_argument("start-maximized")
        WebOptions.add_argument("disable-infobars")
        driver = webdriver.Chrome(executable_path="../../WebDriver/chromedriver", chrome_options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
        #, WebOptions, service_args, desired_capabilities, service_log_path, chrome_options, keep_alive)
        return driver
BrowserDriver = clsWebDriver.ChromeDriver(self=None)

