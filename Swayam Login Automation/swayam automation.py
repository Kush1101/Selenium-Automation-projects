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
#get the site
driver.get("https://swayam.gov.in/")
wait = WebDriverWait(driver,600)

driver.find_element_by_name("submit").click()

#Google login button
google_xpath = '''//*[@id="GoogleExchange"]'''
google = wait.until(EC.presence_of_element_located((By.XPATH,google_xpath)))
google.click()

#Username on google login
username_xpath = '//*[@id="identifierId"]'
username = driver.find_element_by_xpath(username_xpath)
email = 'kushagra.nptel@gmail.com'
username.send_keys(email)
#next button
nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]') 
nextButton[0].click() 

pwd = '2_Akrs@26174'
password_xpath = '//*[@id ="password"]/div[1]/div / div[1]/input'
passWordBox = wait.until(EC.element_to_be_clickable((By.XPATH,password_xpath)))
passWordBox.send_keys(pwd)
#next button
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]') 
nextButton[0].click() 
#BINGO!

print("Successfully logged in!")
#wait until loading finishes
wait2 = WebDriverWait(driver,600)

#dropdown 
dropdown_path = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a'
dropdown = wait2.until(EC.presence_of_element_located((By.XPATH,dropdown_path)))
dropdown.click() 

#my courses tab
mycourse_path = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li[2]/a' 
mycourse = wait2.until(EC.presence_of_element_located((By.XPATH,mycourse_path)))
mycourse.click()

#Did it!
print("Your courses tab is now open! Thank You!!")
