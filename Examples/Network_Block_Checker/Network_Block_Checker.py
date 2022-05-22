#Example Script Network Block Checker Selenium - Landen Fisher - 4/23/2022

#Import OS
import os
#Import Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#Import REGEX
import re
#Import Sleep
import time

#User VARS
"""
Blocked Port String Goes Here, If It Finds This Redirect It Will Print Blocked
"""
Blocked_String = "https://localhost:6543/"
"""
Time To Wait For Page To Appear
"""
Time_EC = 5

#Chrome Options (Extra Things For The Driver To Do On Start)
options = webdriver.ChromeOptions()
#Start With Window Maximized (Simple Detection Avoidance)
options.add_argument("start-maximized")
#Start With No Useless Popups (Simple Detection Avoidance)
options.add_argument("disable-infobars")
#Start With No Extensions (Simple Detection Avoidance)
options.add_argument("--disable-extensions")
#Start With No Random Warnings (Prefrence Not Required)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Find The Main Directory That This Script Is In 
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

#Add This Directory To /chromedriver.exe To Try To Find The Driver
WebDriverPath = MAIN_DIR + '/chromedriver.exe'

#Get Site To Check
User_STR = input("Site To Check: ") 

#Define Our Driver And Pass In Our Options And Location Of Chromedriver
driver = webdriver.Chrome(options=options, executable_path=WebDriverPath)

#Goto Site To Check
driver.get(User_STR)

#Wait x Seconds Till Link Is Loaded
time.sleep(Time_EC)

#Get Redirect URL If Blocked
Current_Driver_Link = driver.current_url

#Blocked String Checker
Blocked = re.findall(Blocked_String, Current_Driver_Link)

#Check If Blocked On Network
if (Blocked):
    print("Blocked")
else:
    print("UnBlocked")
