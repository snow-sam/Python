
from InstagramAPI import InstagramAPI
from time import sleep
api = InstagramAPI('teste131570', 'samucas5')
api.login()
teste = []

api.getUsernameInfo(18271137076)




def urlposts(userid, lista,x,y):
    api.getUserFeed(userid)
    result = api.LastJson
    lista.append(result['items'][x]['image_versions2']['candidates'][y]['url'])


def pegarposts(userid,size,lista):
    for i in range(0,size):
        urlposts(userid,lista,i,0)
        urlposts(userid,lista,i,1)

def pegarid(nome):
    api.searchUsername(nome)
    result = api.LastJson
    print(result['user']['pk'])

def checartamanho(userid):
    api.getUserFeed(userid)
    result = api.LastJson
    size = 0
    local = []
    for i in range(len(result['items'])):
        if 'image_versions2' in result['items'][i]:
            size += 1
            local.append(i)
    print(size, local)

pegarposts(2346516382,12,teste)

print(teste, len(teste))