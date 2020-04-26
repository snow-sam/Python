from InstagramAPI import InstagramAPI
from time import sleep

def sigo():
    api = InstagramAPI('teste131570', 'samucas5')
    api.login()

    result = api.getTotalFollowings(18271137076)

    for user in result:
        with open ('sigo.txt', 'a') as arquivo:
            arquivo.write(str(user['pk']) + '\n')


