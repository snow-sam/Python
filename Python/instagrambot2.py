import pprint
from Funções import *
from InstagramAPI import InstagramAPI
from time import sleep
import wget

api = InstagramAPI('_life.motivation', 'samucas5')
api.login()
def pesquisar():
    dicionario = {}
    n = input('Pesquisar quantas pessoas? ')
    for i in range(int(n)):
        resposta = input('Usuario: ')
        try:
            api.searchUsername(resposta)
            result = api.LastJson
            pk = result['user']['pk']
            dicionario[resposta] = pk
            return dicionario
        except:
            print('Erro')
    


dic = pesquisar()

def pegarfeed(username):
    dicionario = {}
    try:
        api.getUserFeed(dic[username])
        result = api.LastJson
        
    except:
        print('Erro')


