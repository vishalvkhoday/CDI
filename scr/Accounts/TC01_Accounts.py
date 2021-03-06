'''
Created on Mar 15, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date


strAccountName = "Turntable Testing Company"

@allure.title("Validate Accounts navigation & verify page object ")
def test_Accounts ():
    try:
        LaunchBrowser()
        fn_CaptureScreenShot("Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        sleep(2)
        fn_rptStepDetails("Pass", "Before navigating to Accounts page")
        fn_Search_n_Navigate_Accounts_Page(strAccountName)
        fn_NavigateTo_QuotesPage()
        fn_CaptureScreenShot("Pass", "Quote page navigation completed!!!")
        sleep(5)
        fn_ClickOnNewQuote()
#         fn_VerifyQuotePage()
        sleep(5)
        fn_EnterQuoteSummaryInfo()
        
        fn_CaptureScreenShot("Pass", "Completed !!!")
        assert True
        fn_closeBrowser()
    except:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report")
        fn_closeBrowser()
        
        
# test_Accounts()