'''
Created on Mar 15, 2020

@author: DELL
'''

import pytest
from Lib.ReportFunction import * 
# from Lib.WebDriver import BrowserDriver
from allure_pytest import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import  ElementNotVisibleException
from time import sleep
from random import randint
from datetime import datetime

def ChromeDriver():
    try:
        WebOptions = webdriver.ChromeOptions()
        WebOptions.add_argument("start-maximized")
        WebOptions.add_argument("disable-infobars")
        driver = webdriver.Chrome(executable_path="../../WebDriver/chromedriver", chrome_options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
        #, WebOptions, service_args, desired_capabilities, service_log_path, chrome_options, keep_alive)
        return driver
    except:
        assert False
Browser =ChromeDriver()


def fn_objExist(brwObj):
    intcount =0
    while True:
        try:
            if brwObj.is_displayed() or brwObj.is_enabled() == True:
                rptStepDetails("Object exist hence exiting")
                break
            else:
                sleep(3)
                intcount =intcount+1
                if intcount >= 15:
                    break
                else:
                    rptStepDetails("Waiting for object to load.....")
        except:
                sleep(3)
                intcount =intcount+1
                if intcount >= 15:
                    break
                rptStepDetails("object not found..... Still waiting")
    

def fn_RandString(intlen):
    str_sample="abcdefghijklmnopqrstuvwxyz"
    ret_str =""
    try:
        for i in range(0,intlen):
            intrand =randint(0,25)
            ret_str =ret_str+str_sample[intrand]
    except:
        print("Error while generating random string")
    return ret_str
    
def getWindowName():
    lstwnd =Browser.window_handles
    if len(lstwnd)>1:
        return lstwnd
    
    
@allure.step('Browser Launched')    
def LaunchBrowser():
    try:
        winName = getWindowName()
        Browser.switch_to.window(winName[1])
        Browser.close()
        Browser.switch_to.window(winName[0])
        Browser.get("https://tcdi-test.crm.dynamics.com/main.aspx?forceUCI=1&pagetype=apps")
        sleep(5)
        fn_objExist(Browser.find_element_by_id("i0116"))
        Browser.find_element_by_id("i0116").send_keys("test.fieldsales@cditechnologies.com")
        sleep(5)
        Browser.find_element_by_id("idSIButton9").click()
        fn_objExist(Browser.find_element_by_id("i0118"))
        Browser.find_element_by_id("i0118").send_keys("Tr0x@CRM")
        sleep(5)
        fn_objExist(Browser.find_element_by_id("idSIButton9"))
        Browser.find_element_by_id("idSIButton9").click()
        rptStepDetails("Clicked on sign on button")
        fn_objExist(Browser.find_element_by_id("idBtn_Back"))
        Browser.find_element_by_id("idBtn_Back").click()
        sleep(10)
        WebDriverWait(Browser,40).until(EC.element_to_be_clickable((By.ID,"AppLandingPage")))
        fn_objExist(Browser.find_element_by_id("AppLandingPage"))
        Browser.switch_to.frame("AppLandingPage")
        fn_objExist(Browser.find_element_by_xpath('//*[@id="AppDetailsSec_1_Item_1"]/div[1]'))
        Browser.find_element_by_xpath('//*[@id="AppDetailsSec_1_Item_1"]/div[1]').click()
        Browser.switch_to.window(winName[0])
        sleep(20)
        print("Browser Launch completed !!!!")

        assert True
    except:
        assert False
        
@allure.step("Clicked on Accounts link on left panel")
def fn_NavigateTo_AccountsPage():
    try:
        print("Navigate Account page function started ************")
        WebDriverWait(Browser,120).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sitemap-entity-New_Account']/div[1]")))
        fn_objExist(Browser.find_element_by_xpath("//*[@id='sitemap-entity-New_Account']/div[1]"))
        Browser.find_element_by_xpath("//*[@id='sitemap-entity-New_Account']/div[1]").click()
        sleep(10)
        WebDriverWait(Browser,120).until(EC.element_to_be_clickable((By.ID,"quickFind_text_1")))
        fn_objExist(Browser.find_element_by_id("quickFind_text_1"))
        Browser.find_element_by_id("quickFind_text_1").send_keys("Turntable Testing")
        Browser.find_element_by_id("quickFind_button_1").click()
        WebDriverWait(Browser,120).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Turntable Testing Company")))
        fn_objExist(Browser.find_element_by_partial_link_text("Turntable Testing Company"))
        Browser.find_element_by_partial_link_text("Turntable Testing Company").click()
        assert True
    except:
        assert False

@allure.step("Clicked on Quote link in left panel")
def fn_NavigateTo_QuotesPage():
    print("Quote function started")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sitemap-entity-Home_8E2112DC-AD90-40F5-BEBE-0A8D80785D75']/div")), "Clicked on Home icone")
    WebDriverWait(Browser,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sitemap-entity-NewSubArea_f171d33']/div[1]")), "Quotes link Clicked")
    Browser.find_element_by_xpath("//*[@id='sitemap-entity-NewSubArea_f171d33']/div[1]").click()

@allure.step("Click on Quote button")
def fn_ClickOnNewQuote():
    print("Click on new quote started")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='quote|NoRelationship|HomePageGrid|Mscrm.NewRecordFromGrid11']/button[1]")), "Waiting for Quote Icon")
    fn_objExist(Browser.find_element_by_xpath("//*[@id='quote|NoRelationship|HomePageGrid|Mscrm.NewRecordFromGrid11']/button[1]"))
    Browser.find_element_by_xpath("//*[@id='quote|NoRelationship|HomePageGrid|Mscrm.NewRecordFromGrid11']/button[1]").click()

@allure.step("Verify Quote page")    
def fn_VerifyQuotePage():
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[1]")), "Waiting for Summary Tab")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[2]")), "Waiting for Shipping Tab")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[3]")), "Waiting for Products Tab")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[4]")), "Waiting for Details Tab")
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[5]")), "Waiting for Activities Tab")

@allure.step("Entering summary info")
def fn_EnterSummaryInfo():
    strtodayTM=datetime.today()    
    strtodayTM=str(strtodayTM).replace("-","").replace(" ","").replace(":","").replace(".","")
    strQuoteName = fn_RandString(8)
    strQuoteName = str(strQuoteName) + strtodayTM
    WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[1]")), "Waiting for Summary Tab")
    Browser.find_element_by_xpath("//input[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-122-name6-name.fieldControl-text-box-text']").send_keys(fn_RandString(8))
    