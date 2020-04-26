from InstagramAPI import InstagramAPI
from time import sleep


def unfollow():
    api = InstagramAPI('teste131570', 'samucas5')
    followers= []
    api.login()
    api.getSelfUsersFollowing()
    result = api.LastJson
    for user in result['users']:
        followers.append({'pk':user['pk']})



    for i in followers:
        api.unfollow(i['pk'])
        print ('Dando Unfollow')
        sleep(36)
