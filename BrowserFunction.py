'''
Created on Dec 20, 2020

@author: DELL
'''

from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pytest import fixture
from ReportFunction import * 
from time import sleep
from random import randint
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import allure_pytest
import allure


@pytest.fixture(scope='function')
def ChromeDriver():
    try:
        WebOptions = webdriver.ChromeOptions()
        WebOptions.add_argument("start-maximized")
        WebOptions.add_argument("disable-infobars")
#         driver = webdriver.Chrome(executable_path="C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver", options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
        driver = webdriver.Chrome(executable_path="C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver", chrome_options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
        return driver
    except Exception as e:
        print(e)
        assert False

