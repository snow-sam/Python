from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://pt.shopify.com/ferramentas/gerador-nomes-para-empresas')

driver.find_element_by_xpath('/html/body/div[4]/main/section[1]/div/div/section/form/div/div/label/input').send_keys('doce')
driver.find_element_by_xpath('/html/body/div[4]/main/section[1]/div/div/section/form/div/div/button').click()
nomes = driver.find_elements_by_class_name('business-name-button__name')

for nome in nomes:
    print(nome.text)