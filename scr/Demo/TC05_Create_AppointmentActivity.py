'''
Created on Nov 29, 2020

@author: DELL
'''


from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

strAccountName = "Turntable Testing Company"

@allure.title("Validate Create Appointment Activity")
def test_CreateAppointmentActivity():
    Browser=ChromeDriver()
    try:
        LaunchBrowser(Browser)
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        fn_ClickActivitiesLink(Browser)
        fn_Click_AppointmentButton(Browser)
#         fn_EnterAppointmentDetails(strAccountName)
        fn_closeBrowser(Browser)
    except Exception as e:
        fn_CaptureScreenShot(Browser,"Fail", "Error occured while executing error {}".format(e))
        fn_closeBrowser(Browser)
        
# test_CreateAppointmentActivity()