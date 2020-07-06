import os
def limparlista():

    newlist = []
    with open('usuarios.txt', 'r') as f:
        usuarios = [line.strip() for line in f]
    
    with open('seguidos.txt', 'r') as f:
        seguidos = [line.strip() for line in f]

    with open('sigo.txt', 'r') as f:
        sigo = [line.strip() for line in f]

    jafoi = 0

    for user in usuarios:
        if user in sigo or user in seguidos:
            jafoi += 1
            print('Users Repetidos: ' ,jafoi)
        else:
            newlist.append(user)

    for pessoa in newlist:
        with open('usuariosn.txt', 'a') as arquivo:
            arquivo.write(str(pessoa)+ '\n')
    return


limparlista()
