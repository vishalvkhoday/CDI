'''
Created on May 3, 2020

@author: DELL
'''

import pytest
import allure
import allure_pytest
from time import sleep
from allure_commons.reporter import AllureReporter
import random

@allure.description("This is test case 1 to be printed on the report")
@allure.step("This is test step")
def test_1():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase1.com")
    sleep(random.randint(0,36))
    assert True

@allure.description("This is test case 2 to be printed on the report")
@allure.step("This is test step")
@allure.label("This is lable in testcase 2")
@allure.story("This is the story")
def test_2():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase2.com")
    allure.label("This is lable in testcase 2")
    sleep(random.randint(0,36))
    assert True

@allure.description("This is test case 3 to be printed on the report")
@allure.step("This is test step")
def test_3():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase3.com")
    sleep(random.randint(0,36))
    assert True
 
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase4.com")
def test_4():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase4.com")
    sleep(random.randint(0,36))
 
 
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase6.com")
def test_6():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase6.com")
    sleep(random.randint(0,36))
    assert False
 
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase1.com")
def test_7():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    sleep(random.randint(0,36))
    assert True
 
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase1.com")
def test_8():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    sleep(random.randint(0,36))
    assert True
     
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.description_html("This is HTML Description to be displayed")
def test_9():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    sleep(random.randint(0,36))
    assert True
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.description_html("This is HTML Description to be displayed")
def test_10():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    assert True
     
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.title(test_title="This is testcase 11 with title which will fail")
def test_11():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure_pytest.plugin.allure.step(title="This is the plugin title")
    sleep(random.randint(0,36))
    assert True
    
     
     
@allure.description("This is test descript to be printed on the report")
# @allure.step("This is test step")
@allure.description_html("This is HTML Description to be displayed")
def test_12():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    allure_pytest.plugin.allure.step(title="This is the plugin title")
    assert True
     
@allure.description("This is test descript to be printed on the report")
@allure.title(test_title="This is testcase nos 13")
@allure_pytest.plugin.allure.step(title="This is the plugin title")
def test_13():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    assert True
    