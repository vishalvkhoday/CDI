'''
Created on Nov 20, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

strContactName="vishal"

@allure.severity(severity_level="CRITICAL")
@allure.story("Search for contact from user input")
@allure.title("Search for contact ")
def test_SearchContact():
    Browser=ChromeDriver()
    try:
        LaunchBrowser(Browser)
        fn_rptStepDetails("Pass", "After launching Browser !!!")
        fn_ClickContactsLink(Browser)
        fn_rptStepDetails("Pass", "After Clicking on Contact!!!")
        fn_SearchContact(Browser,strContactName)
        sleep(5)
        fn_rptStepDetails("Pass", "After searching Contact!!!")
        fn_closeBrowser(Browser)
    except Exception as e:
        fn_CaptureScreenShot(Browser,"Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser(Browser)
        assert False
    
# test_SearchContact()