from selenium import webdriver
from time import sleep
import json
import random
import os


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/emailsignup/?hl=pt-br')
sleep(3)
email = driver.find_element_by_class_name('_2hvTZ pexuQ zyHYP').send_keys('sjyfbgykfkjadjh@yahoo.com')
nome = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input').send_keys('Gustavo Medeiros')
usuario = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input').send_keys('flanelinha.sintilante.')
senha = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input').send_keys('samucas5')
cadastrar = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()







