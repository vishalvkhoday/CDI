'''
Created on Nov 20, 2020

@author: DELL
'''

from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

strContactName="vishal"

@allure.step("Search for contact ")
def test_SearchContact():
    
    LaunchBrowser()
    fn_ClickContactsLink()
    fn_SearchContact(strContactName)
    
    
test_SearchContact()