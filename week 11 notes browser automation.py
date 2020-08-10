# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:50:03 2020

@author: DeLL
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
#driver = webdriver.Chrome("C:/Users/DeLL/Desktop/Downloads/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target='Kush'
string = "Hi"
x_arg = '//span[contains(@title,'+target+')]'
target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()
input_box = driver.find_element_by_class_name('_1Plpp')
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
print("Messages Sent!!")
