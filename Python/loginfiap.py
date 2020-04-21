from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('C:/Users/Simome/Desktop/sitenovo/chromedriver')
driver.get("https://www2.fiap.com.br/")
sleep(3)
driver.find_element_by_xpath('/html/body/section/div[2]/form/div[1]/div[1]/input').send_keys('86482')
driver.find_element_by_xpath('/html/body/section/div[2]/form/div[1]/div[2]/input').send_keys('142002')
driver.find_element_by_xpath('/html/body/section/div[2]/form/div[2]/input').click()
