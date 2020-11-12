'''
Created on Mar 15, 2020

@author: DELL
'''

import allure
import allure_commons
import allure_pytest
from Commonfunction import *


@allure.step("{TestStatus},{TestStep}")
def fn_rptStepDetails(TestStatus=None,TestStep=None):
    try:
        
        if TestStatus == "Pass" or TestStatus =="pass":
    #         allure.attach.file("C:/Users/DELL/Downloads/image.png", "ScreenShot", attachment_type=None, extension="PNG")
    #         allure.attach.file("../ScreenShot.PNG", "ScreenShot", attachment_type=None, extension="PNG")
            TestStatus=None
            TestStep=None
            assert True
        else:
            allure.attach.file("../ScreenShot.PNG", TestStep, attachment_type=None, extension="PNG")
            assert False
    
    except Exception as e:
        fn_rpts_StepWith_Screenshot("Fail", e)
        
@allure.description("{Description}")
def fn_rptTestDescription(Description=None):
    assert True

@allure.epic("{UserStory}")
def fn_rptUserStory(UserStory=None):
    assert True
    
@allure.testcase("{TC_Name}")
def fn_rptTC_Name(TC_Name=None):
    print(TC_Name)
    assert True

@allure.title("{TC_Title}")
def fn_rptTC_Title(TC_Title=None):
    print(TC_Title)
    assert True
    
@allure.step("*******ScreenShot {TestStep} **********")
def fn_rpts_StepWith_Screenshot(TestStatus,TestStep):
    try:
        if TestStatus == "Pass" or TestStatus =="pass":
            fn_rptStepDetails(TestStatus, TestStep)
            allure.attach.file("../ScreenShot.PNG", TestStep, attachment_type=None, extension="PNG")
            assert True
        elif TestStatus == "Fail" or TestStatus =="fail":
            
            allure.attach.file("../ScreenShot.PNG", TestStep, attachment_type=None, extension="PNG")
            assert False
    
    except Exception as e:
        print(e)
        
    
    