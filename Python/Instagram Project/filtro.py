import os
def limparlista():
    usuarios = []
    sigo = []
    newlist =[]

    usuar = open("usuarios.txt", "r")
    linhas = usuar.readlines()
    for linha in linhas:
        usuarios.append(linha[:-2])
    usuar.close()




    sig = open("sigo.txt", "r")
    linhas = sig.readlines()
    for linha in linhas:
        sigo.append(linha[:-2])
    usuar.close()

    jafoi = 0

    for user in usuarios:
        if user in sigo:
            jafoi += 1
            print('Users Repetidos: ' ,jafoi)
        else:
            newlist.append(user)

    for pessoa in newlist:
        with open('usuariosn.txt', 'a') as arquivo:
            arquivo.write(str(pessoa)+ '\n')


