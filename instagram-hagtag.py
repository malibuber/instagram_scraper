# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:09:03 2020

@author: mehmet
"""

import time
from bs4 import BeautifulSoup
import selenium as se
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import sys


options = se.webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('blink-settings=imagesEnabled=false')  not load images
# options.add_argument('--no-sandbox')
# options.add_experimental_option('excludeSwitches', ['enable-automation']) 
time.sleep(3)
try: 
    browser = se.webdriver.Chrome(ChromeDriverManager().install() , chrome_options= options)
except:
    print("webdriver error")
    
username = "xxxxx@gmail.com"
password = "xxxxxx"    

browser.get("https://www.instagram.com/")

time.sleep(3)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(2)
url = "https://www.instagram.com/explore/tags/"
hashtag = "btc"
url_comp = url + hashtag
browser.get(url_comp)

time.sleep(1)

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()
users = []
time.sleep(1)

user= browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text 
users.append(user)
browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
print(users)
time.sleep(1)
while True:
    # /html/body/div[5]/div[1]/div/div/a
    # /html/body/div[5]/div[1]/div/div/a[2]
    user= browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text 
    users.append(user)
    try:
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        
    except:
        break
    

    time.sleep(1)
print(users)
