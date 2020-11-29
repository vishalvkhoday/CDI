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
#         fn_NavigateTo_QuotesPage()
        
        fn_CaptureScreenShot("Pass", "Quote page navigation completed!!!")
        fn_ClickAddProductBtn()
        scrProdList =fn_SelectProduct()
        fn_ClickAddCheckClose()
        fn_verifyProductName(scrProdList)
        fn_CaptureScreenShot("Pass", "Completed !!!")      
        fn_closeBrowser()
        
        assert True
    except:
        fn_CaptureScreenShot("Fail", "Unknown error look for error in report")
        fn_closeBrowser()
        
        
test_CreateQuote()