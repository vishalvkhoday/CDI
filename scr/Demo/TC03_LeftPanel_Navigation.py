'''
Created on Mar 15, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date


@allure.title("Validate all links in left panel")
def test_CreateQuote ():
    try:
        LaunchBrowser()
        fn_CaptureScreenShot("Pass","After Browser Launch")
        sleep(2)
        fn_ClickHomeLink()
#         fn_ClickRecentLink()
        fn_ClickDashboardsLink()
        fn_ClickActivitiesLink()
        fn_ClickAccountsLink()
        fn_ClickContactsLink()
        fn_ClickOpportunitiesLink()
        fn_ClickQuotesLink()
        fn_CaptureScreenShot("Pass", "Completed !!!")
        fn_closeBrowser()
        assert True
    except:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report")
        fn_closeBrowser()
        assert False
        
        
# test_CreateQuote()