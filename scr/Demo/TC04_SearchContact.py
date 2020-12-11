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

@allure.title("Search for contact ")
def test_SearchContact():
    try:
        LaunchBrowser()
        fn_rptStepDetails("Pass", "After launching Browser !!!")
        fn_ClickContactsLink()
        fn_rptStepDetails("Pass", "After Clicking on Contact!!!")
        fn_SearchContact(strContactName)
        fn_rptStepDetails("Pass", "After searching Contact!!!")
        fn_closeBrowser()
    except Exception as e:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser()
        assert False
    
# test_SearchContact()