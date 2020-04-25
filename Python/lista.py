from InstagramAPI import InstagramAPI
from time import sleep
api = InstagramAPI('teste131570', 'samucas5')
api.login()



usuarios = []

usuar = open("usuarios.txt", "r")
linhas = usuar.readlines()
for linha in linhas:
    usuarios.append(linha[:-2])
usuar.close()

for usuario in usuarios:
    try:
        api.follow(usuario)
        sleep(36)
        print('Follow')
    except:
        print('erro')


