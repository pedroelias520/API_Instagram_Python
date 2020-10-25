# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:22:44 2020

@author: Pedro Elias
"""
import random as random
from random import randint
from selenium import webdriver
from time import sleep
from decimal import Decimal
import time
from progress import Bar

bar = Bar('Processing', max=50)
browser =  webdriver.Firefox(executable_path='C:\geckodriver.exe')
class main:
    def __init__(self): 
        print('O algoritmo está em execução....')
        logIn()
        FollowPeople()
        UnfllowPeople()

def logIn():       
    browser.get('https://www.instagram.com/accounts/login/')
    
    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys("@eu_pedro_sousa")
    password_input.send_keys("drawepic19")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    try:
        login_check = login_button.click()        
    except:
        print('Erro no login')
    sleep(5)
   
def UnfllowPeople():
    browser.get('https://www.instagram.com/pedro_sousa_figueredo/')
    profile_logo_following = browser.find_element_by_xpath("//span[@class='g47SY']")
    profile_logo_following.click()
    number_of_random = randint(0, 20)
    cont_num = 0
    following_button = browser.find_element_by_xpath("//button[text()='Seguindo']")
    for i in following_button:
        if(cont_num<=number_of_random):
            i.click()
            cont_num=cont_num + 1
            bar.next()
        else:
            print("Target Acquired")
    bar.finish()
    
def FollowPeople():       
    not_now = browser.find_element_by_xpath("//button[text()='Agora não']")
    not_now.click()
    browser.implicitly_wait(2)
    not_now = browser.find_element_by_xpath("//button[text()='Agora não']")
    not_now.click()
    
    browser.implicitly_wait(5)
    see_all = browser.find_element_by_xpath("//a[@href ='/explore/people/']")
    see_all.click()
    browser.implicitly_wait(2)    
    infinite = 1
    cont = 0    
    #Get all people to follow
    
    while(infinite == 1):
        number_of_people = randint(0,50)
        print('Number of repetitions')
        print(number_of_people)
        print('=========================')
        #Colect all id's od person
        
        person = browser.find_elements_by_xpath("//button[text()='Seguir']")           
        if (person == ''):
            print('Users not founded')
            break
        
        print('Pessoas')
        print(person)
        print('=========================')                                
        #Follow all person's    
        for i in person:
            if (cont<=number_of_people):
                bar.next()                     
                i.click()   
                cont = cont + 1
            else:                
                print('Target acquired')
                break
    
main()
        
    
