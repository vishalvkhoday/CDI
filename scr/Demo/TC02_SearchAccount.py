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

@allure.title("Validate Accounts Search & navigation with verify page object ")
def test_SearchAccounts ():
    try:
        LaunchBrowser()
#         fn_CaptureScreenShot("Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        fn_Search_n_Navigate_Accounts_Page(strAccountName)
        fn_verifyAccountsPage(strAccountName)
        fn_CaptureScreenShot("Pass", "Completed !!!")
        fn_closeBrowser()
        assert True
    except Exception as e:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser()
        assert False
        
        
# test_SearchAccounts()