#!/usr/bin/env python3
#Alisher Yokubjonov
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 




a_file = open("songs.txt", "r") #List of songs you'd like downloaded
music=[]
for line in a_file:
    line= line.strip() 
    music.append(line) 

missed=[] 
 

def whilenot(xpath): 
    x=0
    while x==0: 
        print('3')
        try: 
            print('1')
            driver.find_element_by_xpath(xpath)
            x=1
            break
        except: 
            print('2')
            continue 
    return 

def xpath(xpath): 
    button= driver.find_element_by_xpath(xpath)
    return button

def byclass(classname): 
    button= driver.find_element_by_class_name(classname)
    return button

def waits(time,xpath): 
    try:
        element = WebDriverWait(driver, time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
    except: 
        print("error occured")
        
     
    

driver=webdriver.Chrome(executable_path='/home/alisher/Desktop/IB/Drivers/chromedriver')
driver.get('https://www.mp3juices.cc/')

try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="query"]'))
    )
except: 
    print("error occured")

for song in music: 
    xpath('//*[@id="query"]').clear()
    xpath('//*[@id="query"]').send_keys(song)
    time.sleep(0.3)
    waits(5, '//*[@id="button"]')
    xpath('//*[@id="button"]').click()
    time.sleep(1)
    if  driver.find_elements_by_xpath("//*[text()='No results. Please try to search another song.']"): 
        continue
    waits(5,'//*[@class="download 1"]')
    xpath('//*[@class="download 1"]').click() 
    waits(30, '//*[text()="The file is ready. Please click the download button to start the download."]')
    xpath('//*[@class="url"]').click()

    try: 
        xpath('//*[text()="Mp3Juices"]')
    except: 
        driver.close() 
    