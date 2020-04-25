from selenium import webdriver
from time import sleep
import json
import random
import os

lista = []


def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open (arquivo , 'r') as arq_json:
            dicionario = json.load(arq_json)
    else:
            dicionario = {}
    return dicionario
def upload_dic(dicionario,arquivo):
    with open(arquivo ,'a') as arq_json:
        json.dump(dicionario, arq_json)


driver = webdriver.Chrome()
driver.get('https://10minutemail.net/?lang=pt-br')

email = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[5]/div[1]/input')

print(email.get_attribute('value'))
