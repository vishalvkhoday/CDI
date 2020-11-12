'''
Created on Mar 15, 2020

@author: DELL
'''

import allure
import allure_commons
import allure_pytest


@allure.step("{TestStatus},{TestStep}")
def rptStepDetails(TestStatus=None,TestStep=None):
    if TestStatus == "Pass" or TestStatus =="pass":
        allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
        assert True
    else:
        allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
        assert False
    
@allure.description("{Description}")
def rptTestDescription(Description=None):
    assert True

@allure.epic("{UserStory}")
def rptUserStory(UserStory=None):
    assert True
    
@allure.testcase("{TC_Name}")
def rptTC_Name(TC_Name=None):
    assert True

@allure.title("{TC_Title}")
def rptTC_Title(TC_Title=None):
    assert True
    