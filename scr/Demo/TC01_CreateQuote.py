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


@allure.title("Validate Quote Creation")
def test_CreateQuote ():
    try:
        LaunchBrowser()
        fn_CaptureScreenShot("Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        sleep(2)
        fn_rptStepDetails("Pass", "Before navigating to Accounts page")
        fn_rptTC_Title("Before navigating to Accounts page")
        fn_NavigateTo_AccountsPage()
        fn_rptTC_Title("After navigating to Accounts page")
        fn_NavigateTo_QuotesPage()
        fn_CaptureScreenShot("Pass", "Quote page navigation completed!!!")
        sleep(5)
        fn_ClickOnNewQuote()
#         fn_VerifyQuotePage()
        sleep(5)
        fn_EnterQuoteSummaryInfo()
        sleep(random.randint(0,15))

        fn_CaptureScreenShot("Pass", "Completed !!!")
        assert True
        fn_closeBrowser()
    except:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report")
        fn_closeBrowser()
        
        
test_CreateQuote()