'''
Created on Mar 15, 2020

@author: DELL
'''

import allure
import allure_commons
import allure_pytest


def rptStepDetails(stepDetails):
    allure.step(stepDetails)
    