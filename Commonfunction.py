'''
Created on Mar 15, 2020

@author: DELL
'''

import pytest
from selenium import webdriver
from pytest import fixture
from ReportFunction import * 
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *


def ChromeDriver():
    try:
        WebOptions = webdriver.ChromeOptions()
        WebOptions.add_argument("start-maximized")
        WebOptions.add_argument("disable-infobars")
        driver = webdriver.Chrome(executable_path="C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver", options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
#         driver = webdriver.Chrome(executable_path="C:/Users/DELL/eclipse-workspace/CDI/WebDriver/chromedriver", chrome_options=WebOptions,service_args=["--verbose", "--log-path=../../Log/ExecutionLogs.log"])
        return driver
    except:
        assert False
Browser =ChromeDriver()


def fn_CaptureScreenShot(Res,Desc):
    try:
        Browser.save_screenshot("../ScreenShot.PNG")    
        fn_rpts_StepWith_Screenshot(Res,Desc)
        assert True
    except Exception as e:
        fn_rpts_StepWith_Screenshot("Fail","Unable to capture Screen shot... {}".format(e))
#         assert False

def fn_objExist(brwObj):
    intcount =0
    while True:
        try:
            if brwObj.is_displayed() or brwObj.is_enabled() == True:
                brwObj.location_once_scrolled_into_view                
                fn_rptStepDetails("Pass","Object exist on page {}".format(brwObj))
                break
            else:
                sleep(3)
                intcount =intcount+1
                if intcount >= 15:
                    break
                else:
                    fn_rptStepDetails("Pass","Waiting for object to load.....")
        except NoSuchElementException as e:
                sleep(3)
                intcount =intcount+1
                if intcount >= 15:
                    break
                fn_CaptureScreenShot("Fail","object not found..... Still waiting {}".format(e))
    

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
        try:
            fn_objExist(Browser.find_element_by_name("loginfmt"))
            Browser.find_element_by_id("i0116").send_keys("test.fieldsales@cditechnologies.com")
            sleep(2)
            WebDriverWait(Browser,140).until(EC.element_to_be_clickable((By.ID,"idSIButton9")))
            Browser.find_element_by_id("idSIButton9").click()
            fn_rptStepDetails("Pass", "Login details entered & clicked on login button")
            WebDriverWait(Browser,140).until(EC.element_to_be_clickable((By.ID,"i0118")))
            fn_objExist(Browser.find_element_by_id("i0118"))
            Browser.find_element_by_id("i0118").send_keys("Tr0x@CRM")
            sleep(2)
            fn_objExist(Browser.find_element_by_id("idSIButton9"))
            Browser.find_element_by_id("idSIButton9").click()
            fn_rptStepDetails("Pass","Clicked on sign on button")
            fn_objExist(Browser.find_element_by_id("idBtn_Back"))
            Browser.find_element_by_id("idBtn_Back").click()
        except:
            fn_rptStepDetails("Pass", "User Already loggedin !!!!") 
        sleep(5)
        fn_rptStepDetails("Pass", "Clicked on NO Button in the popup")
        WebDriverWait(Browser,140).until(EC.element_to_be_clickable((By.ID,"AppLandingPage")))
        fn_objExist(Browser.find_element_by_id("AppLandingPage"))
        Browser.switch_to.frame("AppLandingPage")
        WebDriverWait(Browser,140).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='AppDetailsSec_1_Item_1']/div[1]")))
        
#         fn_objExist(Browser.find_element_by_xpath('//*[@id="AppDetailsSec_1_Item_1"]/div[1]'))
#         Browser.find_element_by_xpath('//*[@id="AppDetailsSec_1_Item_1"]/div[1]').click()
        Browser.find_element_by_xpath("//div[contains(text(),'Field Sales')]").click()
        Browser.switch_to.window(winName[0])
        sleep(20)
        fn_rptStepDetails("Pass", "Logged into application!!!")

        assert len(winName[0])>0
    except Exception as e:
        fn_CaptureScreenShot("Fail", "Failed in Launch browser function {}".format(e))
        assert False
        
@allure.step("Clicked on Accounts link on left panel")
def fn_NavigateTo_AccountsPage():
    try:
        fn_rptStepDetails("Pass", "Navigate Account page function started ************")
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
        fn_CaptureScreenShot("Pass", "Accounts page after click on account link")
        assert True
    except Exception as e:
        fn_CaptureScreenShot("Fail","Error while navigating to Accounts page {}".format(e))
        assert False

@allure.step("Clicked on Quote link in left panel")
def fn_NavigateTo_QuotesPage():
    
    fn_rptStepDetails("Pass", "Quote function started")
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sitemap-entity-Home_8E2112DC-AD90-40F5-BEBE-0A8D80785D75']/div")), "Clicked on Home icone")
    WebDriverWait(Browser,120).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sitemap-entity-NewSubArea_f171d33']/div[1]")), "Quotes link Clicked")
    Browser.find_element_by_xpath("//*[@id='sitemap-entity-NewSubArea_f171d33']/div[1]").click()
    fn_CaptureScreenShot("Pass", "Quote page navigation completed")

@allure.step("Click on Quote button")
def fn_ClickOnNewQuote():
    try:        
        fn_rptStepDetails("Pass", "Click on new quote button on header")
        WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='dataSetRoot_3']/div/div/div/ul/li[2]/button[1]")), "Waiting for Quote Icon")
        fn_objExist(Browser.find_element_by_xpath("//*[@id='dataSetRoot_3']/div/div/div/ul/li[2]/button[1]"))
        Browser.find_element_by_xpath("//*[@id='dataSetRoot_3']/div/div/div/ul/li[2]/button[1]").click()
        fn_CaptureScreenShot("Pass", "After click on new quote button")
    except:
        fn_CaptureScreenShot("Fail","Failed to click on New Quote")
        
@allure.step("Verify Quote page")    
def fn_VerifyQuotePage():
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[1]")), "Waiting for Summary Tab")
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[2]")), "Waiting for Shipping Tab")
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[3]")), "Waiting for Products Tab")
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[4]")), "Waiting for Details Tab")
    WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='ch mj mk nu lh nv nw em d le flexbox']/li[5]")), "Waiting for Activities Tab")

@allure.step("Entering summary info")
def fn_EnterQuoteSummaryInfo():
    try:
        strtodayTM=str(date.today())    
        strtodayTM=str(strtodayTM).replace("-","").replace(" ","").replace(":","").replace(".","")
        strQuoteName = "QA_"+fn_RandString(7)+"_"+fn_RandString(5)+"_"+strtodayTM
        fn_rptStepDetails("Pass", "QuoteName "+strQuoteName)
        WebDriverWait(Browser,130).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-3-name6-name.fieldControl-text-box-text']")), "Waiting for Summary Tab")
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-3-name6-name.fieldControl-text-box-text']").click()
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-3-name6-name.fieldControl-text-box-text']").clear()
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-3-name6-name.fieldControl-text-box-text']").send_keys(strQuoteName)
        sleep(2)
        Browser.find_element_by_xpath('//*[@id="id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-9-customerid8"]').click()
        Browser.find_element_by_xpath('//*[@id="id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-9-customerid8-customerid.fieldControl-LookupResultsDropdown_customerid_1_infoContainer_0_0"]').click()
    #      Enter account name
        WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-9-customerid8-customerid.fieldControl-LookupResultsDropdown_customerid_1_infoContainer_0_0']")), "Waiting for Account Lookup values to appear")
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-9-customerid8-customerid.fieldControl-LookupResultsDropdown_customerid_5_resultsLabel_0_0'][1]").click()
        
        ## Enter memo details
#         Browser.find_element_by_xpath("//textarea[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-26-description6-description.fieldControl-text-box-text']").location_once_scrolled_into_view
#         Browser.find_element_by_xpath("//textarea[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-26-description6-description.fieldControl-text-box-text']").click()
#         Browser.find_element_by_xpath("//textarea[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-26-description6-description.fieldControl-text-box-text']").send_keys("Automation testing kindly ignore")
#         
        ## select category
        Browser.find_element_by_xpath("//button[@class='msos-caret-button']").click()
        WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.ID,"troxcdi_category_item1")),"Waiting for drop down to appear")
    # troxcdi_category_item1 click 1st item
        Browser.find_element_by_xpath("(//div[@class='msos-label-text msos-optionitem-text'])[2]").click()
        sleep(5)
        fn_CaptureScreenShot("Pass", "Quote detils entered")
        Browser.find_element_by_xpath("//button[@class='msos-caret-button']").click()
    #     Enter contact name        
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-13-troxcdi_contactname8-troxcdi_contactname.fieldControl-LookupResultsDropdown_troxcdi_contactname_2_textInputBox_with_filter_new']").click()
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-13-troxcdi_contactname8-troxcdi_contactname.fieldControl-LookupResultsDropdown_troxcdi_contactname_2_textInputBox_with_filter_new']").clear()
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-13-troxcdi_contactname8-troxcdi_contactname.fieldControl-LookupResultsDropdown_troxcdi_contactname_2_textInputBox_with_filter_new']").send_keys('Vishal khoday ')
        WebDriverWait(Browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-13-troxcdi_contactname8-troxcdi_contactname.fieldControl-LookupResultsDropdown_troxcdi_contactname_2_resultsContainer_0_0']")),"Waiting for Contact lookup values to appear")
        Browser.find_element_by_xpath("//*[@id='id-c7a4eb13-1549-ea11-a812-000d3a5a11b0-13-troxcdi_contactname8-troxcdi_contactname.fieldControl-LookupResultsDropdown_troxcdi_contactname_2_resultsContainer_0_0']").click()
        
        sleep(2)
                
    except Exception as e:
        fn_CaptureScreenShot("Fail", "Error while entering quote details {}".format(e))
        
@allure.step("Click on Save button on header")    
def fn_Click_Save_OnHeader():    
    Browser.find_element_by_xpath("//*[@id='quote|NoRelationship|Form|Mscrm.SavePrimary12']/button").click()
    
@allure.step("Browser Closed")
def fn_closeBrowser():
    Browser.quit()
    
@allure.step("Clicked on Home link in left panel")
def fn_ClickHomeLink():
    Browser.find_element_by_xpath("(//*[@title='Go to home page'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='Dashboard_Selector_3486372d-7988-474d-9cf8-8e94504554ef_text-value']")), "Waiting for Home page")
    fn_objExist(Browser.find_element_by_xpath("//span[@id='Dashboard_Selector_3486372d-7988-474d-9cf8-8e94504554ef_text-value']"))
    

@allure.step("Clicked on Recent link in left panel")
def fn_ClickRecentLink():
    Browser.find_element_by_xpath("(//*[@title='Recent items'])[1]").click()
    

@allure.step("Clicked on Dashboards link in left panel")
def fn_ClickDashboardsLink():
    Browser.find_element_by_xpath("(//*[@title='Dashboards'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Trox Field Sales Dashboard')]")), "Waiting for Home page")
    fn_objExist(Browser.find_element_by_xpath("//span[contains(text(),'Trox Field Sales Dashboard')]"))

@allure.step("Clicked on Dashboards link in left panel")
def fn_ClickActivitiesLink():
    Browser.find_element_by_xpath("(//*[@title='Activities'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'My Activities')]")), "Waiting for Activities page")
    fn_objExist(Browser.find_element_by_xpath("//span[contains(text(),'My Activities')]"))

@allure.step("Clicked on Accounts link in left panel")
def fn_ClickAccountsLink():
    Browser.find_element_by_xpath("(//*[@title='Accounts'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'My Accounts')]")), "Waiting for Home page")
    fn_objExist(Browser.find_element_by_xpath("//span[contains(text(),'My Accounts')]"))

@allure.step("Clicked on Contacts link in left panel")
def fn_ClickContactsLink():
    Browser.find_element_by_xpath("(//*[@title='Contacts'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'My Active Contacts')]")), "Waiting for Contacts page")
    fn_objExist(Browser.find_element_by_xpath("//span[contains(text(),'My Active Contacts')]"))
    
@allure.step("Clicked on Opportunity link in left panel")
def fn_ClickOpportunitiesLink():
    Browser.find_element_by_xpath("(//*[@title='Opportunities'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'My Open Opportunities')]")), "Waiting for Opportunities page")
    fn_objExist(Browser.find_element_by_xpath("//span[contains(text(),'My Open Opportunities')]"))
    
@allure.step("Clicked on Quotes link in left panel")
def fn_ClickQuotesLink():
    Browser.find_element_by_xpath("(//*[@title='Quotes'])[1]").click()
    WebDriverWait(Browser,130).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='pa-bv pa-e pa-cp ']")), "Waiting for My Quotes page")
    fn_objExist(Browser.find_element_by_xpath("//span[@class='pa-bv pa-e pa-cp ']"))

