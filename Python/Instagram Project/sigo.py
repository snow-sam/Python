from InstagramAPI import InstagramAPI
from time import sleep

def sigo():
    api = InstagramAPI('_life.motivation', 'samucas5')
    api.login()

    result = api.getTotalSelfFollowings()

    for user in result:
        with open ('sigo.txt', 'a') as arquivo:
            arquivo.write(str(user['pk']) + '\n')

sigo()