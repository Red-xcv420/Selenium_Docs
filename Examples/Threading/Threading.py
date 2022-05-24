"""
Selenium Example For Itterating Tables Or Other Elements That Have The Same XPATH Using Threading - Landen Fisher - 5/22/2022

Site: https://webscraper.io/test-sites/tables
"""

#Import OS

import os
from multiprocessing import Process

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

#Import Color Console - https://pypi.org/project/termcolor/ - pip install termcolor

from termcolor import colored, cprint

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

#Get First Table Left To Right
def Main_Left_To_Right():

    #Make A Var That Is 1 (We Add One Each Time We Do The Loop To Know How Many Times We Have Done The Loop To Find The Next Element With Ease)
    #Starts At 1 To Skip The First Element (The First Element Is A 1) (Uses Indexing So Counter 1 Is Element 2 Example (0,1,2,3,4,5,6,7,8,9) Index Starts At 0)
    Counter = 1

    #Loop To Find The Next Element Forever (Break When Done)
    
    while True:
        
        #Add One To The Number Of Times The Loop Has Completed
        
        Counter += 1

        #---
        #Our Xpath (Starts With Mark, Below Is Mark On The Tables Xpath, Will End With Larry's Xpath)
        
        """
        Example
        /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[1] < Mark
        /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[2] < Otto
        /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[3] < @mdo
        
        This Example Gets Everything In The Row Left To Right, As We Put Counter In The td Part Of Xpath, When You Put Counter In tr It Will Go Top To Bottom In The Row 
        """

        #Put Counter In td
        XPATH = "/html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[" + str(Counter) + "]"
        #---

        #Print Debug Info
        
        print("SYS ON ELEMENT NUMBER: " + str(Counter) + ".. XPATH IS: " + XPATH)
        
        #Try To Find Next Element

        try: 

            #Text From Element Each Time Found (Uses EC To Wait For Page And Element To Apear)
            
            Text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, XPATH))).text
            
            #Print Element Text
            
            cprint(Text, 'green')
        
        #If Can Not Found The Next Element

        except:

            #Print Nothing Else On The Page
            
            cprint("No More On Page...", 'red')
            
            #Close Tab That Is Now Dead
            
            driver.close()
            
            #Stop The Loop
            
            break

#Get First Table Top To Bottom
def Main_Top_To_Bottom():
    
    #Make A Var That Is 0 (We Add One Each Time We Do The Loop To Know How Many Times We Have Done The Loop To Find The Next Element With Ease)

    Counter = 0

    #Loop To Find The Next Element Forever (Break When Done)
    
    while True:
        
        #Add One To The Number Of Times The Loop Has Completed
        
        Counter += 1
        
        #---
        #Our Xpath (Starts With 1, Below Is Mark On The Tables Xpath, Will End With 3's Xpath)
        
        """
        Example
        /html/body/div[1]/div[3]/table[1]/tbody/tr[1]/td[2] < 1
        /html/body/div[1]/div[3]/table[1]/tbody/tr[2]/td[2] < 2
        /html/body/div[1]/div[3]/table[1]/tbody/tr[3]/td[2] < 3 
        
        This Example Gets Everything In The Row Top To Bottom, As We Put Counter In The tr Part Of Xpath, When You Put Counter In td It Will Go Left To Right In The Row 
        """

        #Put Counter In td
        XPATH = "/html/body/div[1]/div[3]/table[1]/tbody/tr[" + str(Counter) + "]/td[2]"
        #---

        #Print Debug Info
        
        print("SYS ON ELEMENT NUMBER: " + str(Counter) + ".. XPATH IS: " + XPATH)
        
        #Try To Find Next Element

        try: 

            #Text From Element Each Time Found (Uses EC To Wait For Page And Element To Apear)
            
            Text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, XPATH))).text
            
            #Print Element Text
            
            cprint(Text, 'green')
        
        #If Can Not Found The Next Element

        except:

            #Print Nothing Else On The Page
            
            cprint("No More On Page...", 'red')
            
            #Close Tab That Is Now Dead
            
            driver.close()

            #Stop The Loop

            break

#Make Start Threadding Function
def Start():
    
    #Close Tab That Opens At Start
    driver.close()   

    #Start Thread One (Thread One is The Main_Left_To_Right Function, In This Example I name It But It Doesnt Do Anything, Its For Ease Of Use (To Be Added On To))
    t = Process(target=Main_Left_To_Right, name= "Thread1")
    
    #Start Thread One
    t.start()

    #Start Thread Two (Thread Two is The Main_Top_To_Bottom Function, In This Example I name It But It Doesnt Do Anything, Its For Ease Of Use (To Be Added On To))
    t2 = Process(target=Main_Top_To_Bottom, name= "Thread2")
    
    #Start Thread Two
    t2.start()

    #Wait Till Thread Ends
    t.join()
    
    #Wait Till Thread Ends
    t2.join()

#Wont Goto Into Detail On This But It Starts The Threads (In The Start Function) When Ran
if __name__ == '__main__':

    #Start Program
    Start()
