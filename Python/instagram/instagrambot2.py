import pprint
from InstagramAPI import InstagramAPI
from time import sleep
api = InstagramAPI('teste131570', 'samucas5')
api.login()
lista = []


api.getUserFeed(8799816785)
result = api.LastJson


for i in range(0,12):
    lista.append(result['items'][i]['image_versions2']['candidates'][0]['url'])

for i in range(0,12):
    lista.append(result['items'][i]['image_versions2']['candidates'][1]['url'])

    
print(lista)
