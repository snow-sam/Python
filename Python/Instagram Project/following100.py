from InstagramAPI import InstagramAPI
from time import sleep


def follow2():
    api = InstagramAPI('_life.motivation', 'samucas5')
    api.login()
    aseguir = int(input('Seguir Quantos Usuarios? '))
    tempo = int(input('Em Quanto Tempo? (Em Minutos)  '))
    tpf = 60/(aseguir/tempo)
    count = 0
    seguidos = []
    with open('usuariosn.txt', 'r') as f:
        usuarios = [line.strip() for line in f]
        for i in range(aseguir):
            try:
                api.follow(usuarios[i])
                count += 1
                print('Usuarios Seguidos', count)
                sleep(tpf)
            except:
                print('Erro em seguir usuario')
            seguidos.append(usuarios[i])
        for pessoa in seguidos:
            with open('seguidos.txt', 'a') as arquivo:
                arquivo.write(str(pessoa)+ '\n')
        print('Foram seguidos hoje: ', count)

follow2()
input(' ')
