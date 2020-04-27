import filtro, follow, unfollow, sigo, userstofollow, os

#Renova a Lista de Pessoas Para Seguir (A fazer: Procurar como deletar um item da lista)
os.remove('sigo.txt')
sigo.sigo()
os.remove('usuariosn.txt')
filtro.limparlista()


#Decide se é pra seguir ou desseguir (Está semi-automatico OBS: Procurar como tranformar em Totalmente Automatico)
with open('state.txt', 'r') as arquivo:
    state = arquivo.readlines()

if state[0] == '0':
    follow.follow()
elif state[0] == '1':
    unfollow.unfollow()
else:
    print('Erro em state')

