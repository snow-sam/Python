from InstagramAPI import InstagramAPI

lista = []

api = InstagramAPI('_life.motivation', 'samucas5')
api.login()

n = input('Quantos usuarios vão ser pesquisados? ')

for name in range(int(n)):
    usuario = input('Usuario a ser pesquisado: ')
    api.searchUsername(usuario)
    result = api.LastJson
    lista.append(result['user']['pk'])

print('')

for item in lista:
    print(item)
input(' ')




