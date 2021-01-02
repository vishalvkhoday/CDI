'''
Created on Mar 15, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

@allure.severity(severity_level="CRITICAL")
@allure.story("This is left panel Navigation test")
@allure.title("Validate all links in left panel")
def test_LeftPanelNavigation ():
    Browser=ChromeDriver()
    try:
        LaunchBrowser(Browser)
        fn_CaptureScreenShot(Browser,"Pass","After Browser Launch")
        sleep(2)
        fn_ClickHomeLink(Browser)
        fn_ClickRecentLink(Browser)
        fn_ClickDashboardsLink(Browser)
        fn_ClickActivitiesLink(Browser)
        fn_ClickAccountsLink(Browser)
        fn_ClickContactsLink(Browser)
        fn_ClickOpportunitiesLink(Browser)
        fn_ClickQuotesLink(Browser)
        fn_CaptureScreenShot(Browser,"Pass", "Completed !!!")
        fn_closeBrowser(Browser)
        assert True
    except Exception as e :
        fn_CaptureScreenShot(Browser,"Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser(Browser)
        assert False
        
        
# test_CreateQuote()