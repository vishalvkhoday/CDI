'''
Created on Mar 15, 2020

@author: DELL
'''
from Commonfunction import *
from BrowserFunction import ChromeDriver
from ReportFunction import *
from time import sleep
import random
from datetime import date

strAccountName = "Turntable Testing Company"


@allure.severity(severity_level="CRITICAL")
@allure.story("Create quote for an accounts")
@allure.title("Validate Quote Creation")
def test_CreateQuote (ChromeDriver):
#     Browser=ChromeDriver()
    try:        
        LaunchBrowser(ChromeDriver)
        fn_CaptureScreenShot(ChromeDriver,"Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        sleep(2)
        fn_ClickQuotesLink(ChromeDriver)
#         fn_ClickOnNewQuote(Browser)
#         fn_EnterQuoteSummaryInfo(Browser)
#         fn_ClickProductTab(Browser)
#         sleep(10)
#         fn_ClickAddProductBtn(Browser)
#         fn_SelectProduct(Browser)
#         fn_ClickAddCheckClose(Browser)
#         sleep(10)
#         fn_Click_Save_OnHeader(Browser)
#         fn_CaptureScreenShot(Browser,"Pass", "Completed !!!")      
        fn_closeBrowser(ChromeDriver)
        assert True
        
    except Exception as e:
        fn_CaptureScreenShot(ChromeDriver,"Fail", "Unknown error look for error in report {}".format(e))
        fn_closeBrowser(ChromeDriver)
        assert False
# test_CreateQuote(ChromeDriver)    
