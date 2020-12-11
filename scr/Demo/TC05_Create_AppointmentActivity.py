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
    try:
        LaunchBrowser()
        fn_rptStepDetails("Pass", "Browser Launched Successfully")
        fn_ClickActivitiesLink()
        fn_Click_AppointmentButton()
#         fn_EnterAppointmentDetails(strAccountName)
        fn_closeBrowser()
    except Exception as e:
        fn_rpts_StepWith_Screenshot("Fail", "Error occured while executing error {}".format(e))
        fn_closeBrowser()
        
# test_CreateAppointmentActivity()