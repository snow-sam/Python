from selenium import webdriver
from time import sleep
from funcoes import funcoes 
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


nomes = ler_arquivo('nomes.json')
numero = random.randrange(0,300)



driver = webdriver.Chrome()
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S1829678565%3A1587512986765156&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input').send_keys('hghhbvdsgf')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input').send_keys('adhfajdasdhgfafd')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/input').send_keys('qqqqjsdjsdjhauyg')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/input').send_keys('samucas5')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/div/div[1]/input').send_keys('samucas5')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span').click()


