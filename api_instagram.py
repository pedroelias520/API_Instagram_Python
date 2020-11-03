# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:22:44 2020

@author: Pedro Elias
"""
import random as random
from random import randint
from selenium import webdriver
from time import sleep
from datetime import datetime






browser =  webdriver.Firefox(executable_path='C:\geckodriver.exe')
browser.maximize_window()
instagram_bases = ['lucasmontano','flutterando','dieegosf','cafeparaprogramar','felipealvesdef','filipedeschamps','geek2zone','_codando_','devmedia.com.br','sujeitoprogramador']
username = "@analise_do_mundo"
password = ""
sound = "task_complete.mp3"

class main:
    def __init__(self): 
        print('Executing...')
        logIn()
        while(True):
            chooser = randint(0,2)                    
            if(chooser == 0):                            
                i = randint(0, len(instagram_bases))                                                                    
                UnfllowPeople()
                browser.refresh()
                UnfllowPeople()
                GetFollowersfrom(instagram_bases[i-1])                
            elif (chooser == 1):                
                UnfllowPeople()
                browser.refresh()
                UnfllowPeople()
                FollowPeople()                
            else:
                UnfllowPeople()
                browser.refresh
                UnfllowPeople()                
            browser.get("https://www.instagram.com/")                  
            time = randint(1800, 3600)
            now = datetime.now()
            current_time =  now.strftime("%H:%M:%S")            
            print("Hora de término de execução:" + current_time)
            print('Tempo de espera: %.0f minutos' % (time/60))
            
            sleep(time)        

def logIn():       
    browser.get('https://www.instagram.com/accounts/login/')
    
    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    try:
        login_check = login_button.click()  
        sleep(5)
        not_now = browser.find_element_by_xpath("//button[text()='Agora não']")
        not_now.click()
        browser.implicitly_wait(2)
        not_now = browser.find_element_by_xpath("//button[text()='Agora não']")
        not_now.click()
    except:
        print('Erro no login')
    sleep(5)
   
def UnfllowPeople():
    browser.get("https://www.instagram.com/" + username[1:] )
    browser.implicitly_wait(5)
    profile_logo_following = browser.find_element_by_xpath("//a[@href='/"+ username[1:] +"/following/']")
    profile_logo_following.click()
    print('Number de pessoas para deseguir')
    number_of_random = randint(20, 50)    
    print(number_of_random)
    print('=========================')
    cont_num = 0
    following_button = browser.find_elements_by_xpath("//button[text()='Seguindo']")
    random.shuffle(following_button)
    for i in following_button:
        if(cont_num<=number_of_random):
            try:
                i.click() 
                sleep(randint(3, 20))
                confirm_button = browser.find_element_by_xpath("//button[text()='Deixar de seguir']")
                confirm_button.click()
                cont_num = cont_num + 1
                porcentage =  (cont_num*100) / number_of_random                
                print("%.0f por centro concluídos" % (porcentage))
            except:
                print('Erro de captura')
        else:
            print("Target Acquired")
    
    
def FollowPeople():       
    
    browser.get("https://www.instagram.com")
    browser.implicitly_wait(5)
    see_all = browser.find_element_by_xpath("//div[text() ='Ver tudo']")
    see_all.click()
    browser.implicitly_wait(2)    
    infinite = 1
    cont = 0    
    #Get all people to follow
    
    while(infinite == 1):
        number_of_people = randint(10,20)
        print('Number of repetitions')
        print(number_of_people)
        print('=========================')
        #Colect all id's od person
        
        person = browser.find_elements_by_xpath("//button[text()='Seguir']")  
        random.shuffle(person)  
        
        #Follow all person's    
        for i in person:
            sleep(randint(1, 5))
            if (cont<=number_of_people):                                 
                print(cont)
                i.click()                
                if(browser.find_elements_by_xpath("//button[text()='Deixar de Seguir']")):
                    confirm_button = browser.find_element_by_xpath("//button[text()='Deixar de seguir']")
                    confirm_button.click()
                cont = cont + 1
            else:                
                infinite = 0
                print('Target acquired')
                break
        
        
def GetFollowersfrom(person):
    browser.get("https://www.instagram.com/" + person )
    browser.implicitly_wait(5)
    profile_logo_following = browser.find_element_by_xpath("//a[@href='/"+ person +"/followers/']")
    profile_logo_following.click()
    print('Number of repititons')
    number_of_random = randint(10, 20)    
    print(number_of_random)
    print('=========================')
    cont_num = 0
    following_button = browser.find_elements_by_xpath("//button[text()='Seguir']")
    random.shuffle(following_button)
    
    sleep(randint(0, 5))    
    for i in following_button:
        if(cont_num<=number_of_random):
            try:
                i.click() 
                sleep(randint(3, 20))                
                cont_num=cont_num + 1
                porcentage =  ((cont_num*100) / number_of_random)
                print("%:.0f por cento concluídos" % (porcentage))
            except:
                cont_num=cont_num + 1
                porcentage =  ((cont_num*100) / number_of_random)
                print("%.0f por cento concluídos" % (porcentage))
                print("Erro de captura do botao 'Seguir'")
        else:
            print("Target Acquired")
main()
        
    
