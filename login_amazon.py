# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:08:04 2018
Amazon login
@author: kisku
"""

import selenium, time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.in/')

login_button = driver.find_element_by_xpath('//*[@id="nav-link-yourAccount"]/span[2]')
login_button.click()

user_field = driver.find_element_by_xpath('//*[@id="ap_email"]')
user_field.clear()

user_field.send_keys('ID')


continue_button = driver.find_element_by_xpath('//*[@id="continue"]')
continue_button.click()


time.sleep(1)
user_password = driver.find_element_by_xpath('//*[@id="ap_password"]')
user_password.clear()

user_password.send_keys('Password')

submit_button = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
submit_button.click()
