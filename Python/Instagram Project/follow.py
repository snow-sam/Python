from InstagramAPI import InstagramAPI
from time import sleep
from datetime import datetime
def checkhour():
    now = datetime.now()
    h = now.strftime("%H")
    return h

def checkminute():
    now = datetime.now()
    m = now.strftime("%M")
    return m

def follow():
    usuarios = []
    count = 0
    with open ('usuariosn.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        usuarios.append(linha[:-2])


    api = InstagramAPI('teste131570', 'samucas5')
    api.login()

    for user in usuarios:
        try:
            api.follow(user)
            count += 1
            if checkhour() == '23':
                break
            else:
                sleep(36)
        except:
            print('Erro em seguir usuario')

    with open ('userseguidos.txt', 'w') as arquivo:
        arquivo.write('Foram seguidos hoje: ' + str(count))

    


    
