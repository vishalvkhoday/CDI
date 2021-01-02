'''
Created on Mar 15, 2020

@author: DELL
'''

# from Lib.WebDriver import *
# from Lib.Commonfunction import *
# from Lib.ReportFunction import *

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

strAccountName = "Turntable Testing Company"

@allure.severity(severity_level="CRITICAL")
@allure.story("Validate Accounts search")
@allure.title("Validate Accounts Search & navigation with verify page object ")
def test_SearchAccounts (ChromeDriver):
#     Browser=ChromeDriver()
    try:
        LaunchBrowser(ChromeDriver)
        fn_CaptureScreenShot(ChromeDriver,"Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        fn_Search_n_Navigate_Accounts_Page(ChromeDriver,strAccountName)
#         fn_verifyAccountsPage(Browser,strAccountName)
#         sleep(5)
#         fn_CaptureScreenShot(Browser,"Pass", "Completed !!!")
        fn_closeBrowser(ChromeDriver)
        assert True
    except Exception as e:
        fn_CaptureScreenShot(ChromeDriver,"Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser(ChromeDriver)
        assert False
        
        
# test_SearchAccounts()