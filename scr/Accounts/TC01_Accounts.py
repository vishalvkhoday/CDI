'''
Created on Mar 15, 2020

@author: DELL
'''

# from Lib.WebDriver import *
from Lib.Commonfunction import *
from Lib.ReportFunction import *
import time
from time import sleep

def Accounts ():
    fn_EnterSummaryInfo()
    LaunchBrowser()
    sleep(2)
#     fn_NavigateTo_AccountsPage()
    fn_NavigateTo_QuotesPage()
    fn_ClickOnNewQuote()
    fn_VerifyQuotePage()
    fn_EnterSummaryInfo()
    print("completed")
Accounts()