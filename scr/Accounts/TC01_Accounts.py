'''
Created on Mar 15, 2020

@author: DELL
'''

# from Lib.WebDriver import *
from Lib.Commonfunction import *
from Lib.ReportFunction import *
from time import sleep
import random
from datetime import date


def test_Accounts ():
    try:
        rptTC_Title("Validate Accounts navigation & verify page object ")
        LaunchBrowser()
        rptStepDetails("Pass", "Browser Launched Successfully")
        sleep(2)
        fn_NavigateTo_AccountsPage()
        fn_NavigateTo_QuotesPage()
        fn_ClickOnNewQuote()
#         fn_VerifyQuotePage()
        fn_EnterQuoteSummaryInfo()
        sleep(random.randint(0,15))
        print("completed")
        assert True
    except:
        rptStepDetails("Fail", "Unknown error look for error in report")
        
test_Accounts()