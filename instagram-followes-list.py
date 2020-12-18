# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:59:36 2020

@author: mehmet
"""

# photo url https://www.instagram.com/p/CIlWbVLKMSm/


import time
from bs4 import BeautifulSoup
import selenium as se
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import sys

count = []
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
    
username = "xxxx@gmail.com"
password = "xxxxx"    

browser.get("https://www.instagram.com/")

time.sleep(3)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)
# url = "https://www.instagram.com/p/CHNut9qlD4Z/"
url  = "https://www.instagram.com/eralpsoftware/"
browser.get(url)
time.sleep(2)
follower_count = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

time.sleep(2)
# span class="Jv7Aj mArmR MqpiF"
scr1 = browser.find_elements_by_css_selector("a.notranslate")
for i in scr1:
    count.append(i.text)
# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)  
scr1[-1].location_once_scrolled_into_view
while True:
    try:
        tmp = scr1
        scr1[-1].location_once_scrolled_into_view
    except:
        print("break")
            
    
    scr1 = browser.find_elements_by_css_selector("a.notranslate")
    time.sleep(1)
    try: 
        print(len(scr1))
        if len(scr1) >= int(follower_count) :
            print("break1")     
            print(scr1[-1].text , "*----*" ,tmp[-1].text)
            break
    except:
        print("pass")
all_src = browser.find_elements_by_css_selector("a.notranslate")
print(len(all_src))
count = list(set(all_src))
new_list = []
for i in count:
    if i.text != "":
        new_list.append(i.text)
    




