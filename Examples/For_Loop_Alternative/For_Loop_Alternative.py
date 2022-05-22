"""
Selenium Example For Iterating Tables Or Other Elements That Have The Same XPATH - Landen Fisher - 5/22/2022

Site: https://webscraper.io/test-sites/tables
"""

#Import OS

import os
from tkinter import X

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

#Define Our Driver And Pass In Our Options And Location Of Chromedriver

driver = webdriver.Chrome(options=options, executable_path=WebDriverPath)

#Goto Link

driver.get("https://webscraper.io/test-sites/tables")

#Make A Var That Is 0 (We Add One Each Time We Do The Loop To Know How Many Times We Have Done The Loop To Find The Next Element With Ease)

Counter = 0

#Loop To Find The Next Element Forever (Break When Done)

while True:
    
    #Add One To The Number Of Times The Loop Has Completed
    
    Counter += 1
    
    #---
    #Our Xpath (Starts With Mark, Below Is Mark On The Tables Xpath, Will End With Larry's Xpath)
    
    """
    Example
    /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[1] < 1
    /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[2] < Mark
    /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[3] < Otto
    /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[4] < @mdo
    
    This Example Gets Everything In The Row Left To Right, As We Put Counter In The td Part Of Xpath, When You Put Counter In tr It Will Go Top To Bottom In The Row 
    """

    #Put Counter In td
    XPATH = "/html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[" + str(Counter) + "]"
    #---

    #Print Debug Info
    
    print("SYS ON ELEMENT NUMBER: " + str(Counter) + ".. XPATH IS: " + XPATH)
    
    #Try To Find Next Element

    try: 

        #Text From Element Each Time Found (Uses EC To Wait For Page And Element To Appear)
        
        Text = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, XPATH))).text
        
        #Print Element Text
        
        print(Text)
    
    #If Can Not Found The Next Element

    except:

        #Print Nothing Else On The Page
        
        print("No More On Page...")
        
        #Stop The Loop
        
        break
