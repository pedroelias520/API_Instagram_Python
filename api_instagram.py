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
from bs4 import BeautifulSoup as bs
import requests
import numpy as np






browser =  webdriver.Firefox(executable_path='C:\geckodriver.exe')
browser.maximize_window()
users = []
instagram_bases = ['brito_michelli','anabneri','erickwendel_','marcoshenrique.dev','filipealvesdef','lucasmontano','flutterando','dieegosf','cafeparaprogramar','filipedeschamps','geek2code','codandoclub','devmedia.com.br','sujeitoprogramador','felipeodev','diariodeti','oprogramador_','adsdepressao','carinhadoti','tidadepressao','programadorsonambulo']
username = "@codezone_oficial"
password = "#@Java_6118@#"
URL = "http://www.instagram.com/{}/"


class main:
    def __init__(self):         
        logIn()
        while(True):
            data = scrape_data(username[1:])                                   
            chooser = randint(0, 4)      
            followers = int(data['Followers'])
            data = int(data['Following'])                        
            if(data <= followers/4):
                print('Numero de seguidores baixo, seguindo outros...')
                chooser = 0
            if(data > followers/4):
                print('Seguidores demais, deseguindo alguns')
                chooser = 4
           
                     
            if(chooser == 0):       
                print("Seguir 2x , indice : %i" % (chooser))                                     
                like_user_photo()
                i = randint(0, len(instagram_bases))                                                                                    
                browser.refresh()   
                GetFollowersfrom(instagram_bases[i-1])   
                i = randint(0, len(instagram_bases))        
                sleep(randint(2, 5))
                GetFollowersfrom(instagram_bases[i-1])   
                i = randint(0, len(instagram_bases))        
                sleep(randint(2, 5))
                GetFollowersfrom(instagram_bases[i-1])     
                sleep(randint(2, 5))                
            elif (chooser == 1 or chooser == 2):  
                print("Deseguir 1x e Seguir 2x, indice : %i" %(chooser))                                     
                i = randint(0, len(instagram_bases))   
                UnfllowPeople()                
                browser.refresh()
                sleep(randint(2, 5))
                UnfllowPeople()                
                browser.refresh()
                sleep(randint(2, 5))
                i = randint(0, len(instagram_bases)) 
                GetFollowersfrom(instagram_bases[i-1])
                browser.refresh()
                sleep(randint(2, 5))
                i = randint(0, len(instagram_bases)) 
                GetFollowersfrom(instagram_bases[i-1])      
                sleep(randint(2, 5))
                i = randint(0, len(instagram_bases)) 
                GetFollowersfrom(instagram_bases[i-1])
                like_user_photo()
            else:
                print("Deseguir 3x, indece: %i" % (chooser))                                                    
                UnfllowPeople()
                like_user_photo()
                browser.refresh                
                sleep(randint(2, 5))
                UnfllowPeople()
                browser.refresh
                sleep(randint(2, 5))
                UnfllowPeople()
                sleep(randint(2, 5))                         
            browser.get("https://www.instagram.com/")                  
            time = randint(1800, 7200)
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
def parse_data(s):    
    data= {}
    s = s.split("-")[0]
    s = s.split(" ")
    
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    
    return data
        
def scrape_data(username):
    r = requests.get(URL.format(username))
    
    s = bs(r.text,"html.parser")
    
    meta = s.find("meta",property="og:description")
    
    return parse_data(meta.attrs['content'])
 
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
    
def search_users():
    browser.get("https://www.instagram.com/explore/people/suggested/")
    sleep(randint(0, 5))
    
    for user in browser.find_elements_by_css_selector("div.Igw0E.IwRSH.YBx95.vwCYk"):
        users.append(user.find_element_by_css_selector('a').get_attribute('title'))             
    keyword = (randint(0, len(users)))
    try:
        browser.get("https://www.instagram.com/"+users[keyword -1]+"/")        
        print("Successfully searched for: " + users[keyword -1]+"/")
    except :
        print("Search failed")
def search_users_from_person():
    i = randint(0, len(instagram_bases))        
    browser.get("https://www.instagram.com/" + instagram_bases[i-1] )
    browser.implicitly_wait(5)
    profile_logo_following = browser.find_element_by_xpath("//a[@href='/"+ instagram_bases[i-1] +"/followers/']").click()        
    sleep(randint(0, 5))
    
    for user in browser.find_elements_by_css_selector("div.Igw0E.IwRSH.YBx95.vwCYk"):
        users.append(user.find_element_by_css_selector('a').get_attribute('title')) 
        random.shuffle(users)            
    keyword = (randint(0, len(users)))
    try:
        browser.get("https://www.instagram.com/"+users[keyword -1]+"/")        
        print("Successfully searched for: " + users[keyword -1]+"/")
    except :
        print("Search failed")
                
def like_user_photo():
    #In user profile    
    count =  randint(5, 20)
    print("Curtir fotos de %i pessoas" % (count))
    people_to_like = 0
    while(people_to_like<=count):        
        search_users_from_person()   
        rows = np.array(browser.find_elements_by_css_selector("div.Nnq7C.weEfm"))   
        #Seleciona  uma pessoa                              
        user_without_photos = True    
        while(user_without_photos):                                     
            #Capta as fotos no seu perfil
            if(rows.size == 0):
                #Se não houver fotos o processo de busca é refeito e reiniciar o loop
                print("USUÁRIO SEM FOTOS, PROCURANDO UM NOVO...")                
                search_users_from_person()  
                rows = np.array(browser.find_elements_by_css_selector("div.Nnq7C.weEfm"))                  
                user_without_photos = True
            else:
                #Senão clica em uma foto aleatória e quebra o loop
                position = randint(0, len(rows))
                rows[position-1].find_element_by_css_selector("div.v1Nh3.kIKUG._bz0w").click() 
                people_to_like = people_to_like + 1
                user_without_photos = False
        
        has_picture = True
        count_like = randint(2, 10)
        to_like = 0
        print("Quantidade de likes: %i" % (count_like))
        while has_picture:
           like()                
           to_like = to_like + 1
           sleep(randint(0,3))           
           print("Fotos curtidas: %i" % (to_like))
           if(to_like >= count_like):
               has_picture = False 
               print("Limite de curtidas atingido!")               
           else:
               has_picture = has_next_picture()
        try:
            browser.find_element_by_xpath("//button[@class=\"ckWGn\"]").click()
            print("Fots curtidas do link: " + browser.current_url)            
        except:            
            browser.get("https://www.instagram.com/")
    
def like():                
    try:              
        browser.find_element_by_class_name('fr66n').click()
        sleep(randint(0, 3))                        
    except:
        print("Error to like")        
            
            
def has_next_picture():    
    next_button = "//a[text()=\"Próximo\"]"
    try:
        browser.find_element_by_xpath(next_button).click()        
        return True
    except :
        print("Usuário não possui mais fotos")
        return False            
            
           
def FollowPeople():       
    
    browser.get("https://www.instagram.com/explore/people/suggested/")
    browser.implicitly_wait(5)        
    infinite = 1
    cont = 0    
    #Get all people to follow
        
    number_of_people = randint(5,20)
    print('Number of repetitions')
    print(number_of_people)
    print('=========================')
    #Colect all id's od person
        
    person = browser.find_elements_by_xpath("//button[text()='Seguir']")  
    random.shuffle(person)  
        
    #Follow all person's  
    try:
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
                print('Target acquired')
                break
    except:
        print("ERROR TO FOLLOW, CONTINUING THE FLOW...")
        

         
def GetFollowersfrom(person):
    browser.get("https://www.instagram.com/" + person )
    browser.implicitly_wait(5)
    profile_logo_following = browser.find_element_by_xpath("//a[@href='/"+ person +"/followers/']")
    profile_logo_following.click()
    print('Numero de pessoas para seguir')
    number_of_random = randint(5, 20)    
    print(number_of_random)
    print('=========================')
    cont_num = 0
    following_button = browser.find_elements_by_class_name("sqdOP.L3NKy.y3zKF") 
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
                print("Erro de captura do botao 'Seguir'")
        else:
            print("Target Acquired")
main()
        
    
