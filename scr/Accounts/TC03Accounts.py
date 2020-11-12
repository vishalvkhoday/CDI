'''
Created on May 3, 2020

@author: DELL
'''

import pytest
import allure
import allure_pytest
from time import sleep
import random
from allure_pytest.utils import allure_description
from ReportFunction import fn_rptStepDetails


@allure.description("This is test case 1 to be printed on the report")
@allure.step("This is test step")
def test_14():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase1.com")
    sleep(random.randint(0,36))
    assert True

@allure.description("This is test case 2 to be printed on the report")
@allure.step("This is test step")
@allure.label("This is lable in testcase 2")
@allure.story("This is the story")
def test_15():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase2.com")
    allure.label("This is lable in testcase 2")
    sleep(random.randint(0,16))
    assert True
 
@allure.description("This is test case 3 to be printed on the report")
# @allure.step("This is test step 16")
@allure.epic("This is epic text")
def test_16():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase3.com")
    sleep(random.randint(0,16))
    assert True
  
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase4.com")
def test_17():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase4.com")
    sleep(random.randint(0,16))
  
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase6.com")
def test_18():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase6.com")
    sleep(random.randint(0,16))
    assert True
  
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase1.com")
@allure.severity(severity_level="BLOCKER")
def test_19():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    sleep(random.randint(0,36))
    assert True
     
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.testcase("www.testcase1.com")
def test_20():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    sleep(random.randint(0,26))
    assert True
      
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.description_html("This is HTML Description to be displayed")
def test_21():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure.testcase("www.testcase7.com")
    assert True
    sleep(random.randint(0,16))
     
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.severity(severity_level="CRITICAL")
@allure.description_html("This is HTML Description to be displayed")
def test_22():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    assert True
    sleep(random.randint(0,36))
     
      
@allure.description("This is test descript to be printed on the report")
@allure.step("This is test step")
@allure.severity(severity_level="CRITICAL")
@allure.title(test_title="This is testcase 11 with title which will fail")
def test_23():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    allure_pytest.plugin.allure.step(title="This is the plugin title")
    assert True
    sleep(random.randint(0,36))
      
      
@allure.description("This is test descript to be printed on the report")
@allure.description_html("This is HTML Description to be displayed")
@allure.severity(severity_level="CRITICAL")
def test_24():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    allure_pytest.plugin.allure.step(title="This is the plugin title")
    assert True
    sleep(3)
      
 
@allure.description("This is test descript to be printed on the report")
@allure.title(test_title="This is testcase nos 13")
@allure_pytest.plugin.allure.step(title="This is the plugin title")
@allure.severity(severity_level="CRITICAL")
def test_25():
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    assert True
 
 
@allure.step("{Step}")
@allure.severity(severity_level="BLOCKER")
def test_26(Step=None):
    allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    sleep(random.randint(0,36))
    assert True
     
def test_27():
    test_26("This is test step1")
    test_26("This is test step2")
    test_26("This is test step3")
    fn_rptStepDetails("Pass","This is test step1")
#     rptStepDetails("Fail","This is test step2")
#     rptStepDetails("Fail","This is test step3")
     
     