'''
Created on Dec 20, 2020

@author: DELL
'''
from Commonfunction import *
from ReportFunction import *
from time import sleep
import random
from datetime import date

def test_brow():
    LaunchBrowser()
    fn_closeBrowser()
    LaunchBrowser()
    
test_brow()