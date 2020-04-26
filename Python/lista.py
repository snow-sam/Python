from InstagramAPI import InstagramAPI
from time import sleep
api = InstagramAPI('teste131570', 'samucas5')
api.login()
usuarios = []

'''
api.getMediaLikers(2295103064401965110)
result = api.LastJson

for i in result['users']:
    usuarios.append(i['pk'])


print(usuarios)

for usuario in usuarios:
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(str(usuario) + '\n')

