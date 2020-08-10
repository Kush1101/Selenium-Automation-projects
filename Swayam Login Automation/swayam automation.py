# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:23:32 2020

@author: DeLL
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://swayam.gov.in/")
wait = WebDriverWait(driver,600)
driver.find_element_by_name("submit").click()
x_arg = """//*[@id="GoogleExchange"]"""
target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()
arg2 = '//*[@id="identifierId"]'
#username = driver.find_element_by_class_name('')
username = driver.find_element_by_xpath(arg2)
email = 'your email'
username.send_keys(email+Keys.ENTER)
#driver.find_element_by_class_name('VfPpkd-RLmnJb').click()

#wait2 = WebDriverWait(driver,1000)
x_arg2 = '//*[@id="password"]/div[1]/div/div[1]/input'

class_name = 'whsOnd zHQkBf'
#password = driver.find_element_by_class_name(class_name)
password = driver.find_element_by_xpath(x_arg2)
#assword = driver.find_element_by_id("user_password")
#password = wait2.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
#password.click()
#wait2.until(EC.elementToBeClickable(password))
#password.click()
pwd = 'Hidden'
password.send_keys(pwd+Keys.ENTER)
print("Successfully logged in!")
 
#""" //*[@id="password"]/div[1]/div/div[1]/input //*[@id="password"]/div[1]/div/div[1]/input
