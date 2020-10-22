# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:22:44 2020

@author: Pedro Elias
"""
import random as random
from selenium import webdriver
from time import sleep
from decimal import Decimal 

def __init__():
      logIn()
      FollowPeople()
      print('O algoritmo está em execução....')

def logIn():
    browser =  webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/accounts/login/')

    login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    login_link.click()

    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys("@pedro_sousa_figueredo")
    password_input.send_keys("drawepic16")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    try:
        login_check = login_button.click()        
    except:
        print('Erro no login')
    sleep(5)
    
def FollowPeople():   
    browser =  webdriver.Firefox()
    browser.implicitly_wait(5)
    see_all = browser.find_element_by_css_selector("div[class ='_7UhW9 PIoXz qyrsm KV-D4 uL8Hv ']")
    peoples = []
    infinite = Decimal('Infinity')
    
    #Get all people to follow
    
    for i in infinite:        
        number_of_people = random(50)
        for i in number_of_people:
            people_list = browser.find_element_by_css_selector("div[class = 'Igw0E rBNOH eGOV_ ybXk5 _4EzTm XfCBB HVWg4 ']")
            peoples.append(people_list)
        print(peoples)
        sleep(3600)
    
    
        
    
