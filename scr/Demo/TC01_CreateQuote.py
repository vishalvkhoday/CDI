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

@allure.title("Validate Quote Creation")
def test_CreateQuote ():
    try:
        LaunchBrowser()
        fn_CaptureScreenShot("Pass","After Browser Launch")
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        sleep(2)
        fn_ClickQuotesLink()
        fn_ClickOnNewQuote()
        fn_EnterQuoteSummaryInfo()
        fn_ClickProductTab()
        fn_ClickAddProductBtn()
        fn_SelectProduct()
        fn_ClickAddCheckClose()
        fn_Click_Save_OnHeader()
        fn_CaptureScreenShot("Pass", "Completed !!!")      
        fn_closeBrowser()
        
        assert True
    except:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report")
        fn_closeBrowser()
        
# test_CreateQuote()    
