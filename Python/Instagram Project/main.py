import filtro, follow, unfollow, sigo, userstofollow

with open('state.txt', 'r') as arquivo:
    state = arquivo.readlines()

if state[0] == '0':
    follow.follow()
elif state[0] == '1':
    unfollow.unfollow()
else:
    print('Erro em state')
