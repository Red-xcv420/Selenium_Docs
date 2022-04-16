#COMMON IMPORTS
#-------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By```
#-------------------------
#BETTER CODE
#-------------------------
#Typing To Text Boxes
WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here'))).send_keys("text to be typed")

#Clicking Buttons
WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here'))).click()

#Getting Text From Page
Text_From_Element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here'))).text

#Getting Attribute From Element (EXAMPLE SRC)
SRC = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here'))).get_attribute('src')

#OLD METHOD
Button = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here')))
Button.click()

#Other Than Xpath 
Text_From_Element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, 'ID goes here'))).text
#-------------------------

"""
This code is able to wait until element's appear and make code into one line. It is Better than the old more common...
var = driver.find_element_by_id('id')
var.click()
"""
