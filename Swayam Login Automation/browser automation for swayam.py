# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:43:46 2020

@author: DeLL
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:/Users/DeLL/Desktop/Downloads/chromedriver.exe")
driver.get("https://swayam.gov.in/")
wait = WebDriverWait(driver,600)
#target='"SIGN-IN/REGISTER"'
#target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
input_box = driver.find_element_by_class_name("btn btn-primary btn-lg")
input_box.click()