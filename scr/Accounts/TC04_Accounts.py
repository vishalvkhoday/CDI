'''
Created on Oct 25, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
from datetime import date



@allure.title("Validate Left Panel links")
def test_LeftPanel ():
    try:
        
        LaunchBrowser()
        fn_CaptureScreenShot("Pass","After Browser Launch")
        sleep(2)
        fn_ClickHomeLink()
        fn_ClickRecentLink()
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
        
        
        
# test_LeftPanel()