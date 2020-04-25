import pprint
from InstagramAPI import InstagramAPI
from time import sleep
'''
api = InstagramAPI('_life.motivation', 'samucas5')
api.login()
lista = []
captions = []
'''
usuarios = []

usuar = open("usuarios.txt", "r")
linhas = usuar.readlines()
for linha in linhas:
    usuarios.append(linha[:-2])
usuar.close()

print()
