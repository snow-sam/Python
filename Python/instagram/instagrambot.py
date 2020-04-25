from instapy_cli import client
from InstagramAPI import InstagramAPI
import wget
import pprint
from time import sleep
api = InstagramAPI('teste131570', 'samucas5')
api.login()
posts = []
legendas = []
usuarios = []


def legendposts(userid, lista,x):
    api.getUserFeed(userid)
    result = api.LastJson
    lista.append(result['items'][x]['caption']['text'])


def pegarcoments(userid,lista):
    for i in checartamanho(userid):
        legendposts(userid,lista,i)





def urlposts(userid, lista,x):
    api.getUserFeed(userid)
    result = api.LastJson
    try:
        lista.append(result['items'][x]['image_versions2']['candidates'][0]['url'])
    except:
        print(x, 'inexistente')

def pegarposts(userid,size,lista):
    for i in range(0,size):
        urlposts(userid,lista,i)

def pegarid(nome):
    api.searchUsername(nome)
    result = api.LastJson
    print(result['user']['pk'])

def checartamanho(userid):
    api.getUserFeed(userid)
    result = api.LastJson
    local = []
    for i in range(len(result['items'])):
        if 'image_versions2' in result['items'][i]:
            local.append(i)
    return local

#7337345688



def baixarcoments(lista,userid):
    for i in checartamanho(userid):
        with open (str(i)+'.txt', 'w', encoding='utf-8') as coment:
            coment.writelines(lista[i])

def baixarposts(lista,userid):
    for i in checartamanho(userid):
        try:
            wget.download(lista[i])
        except:
            print(i, 'inexeistente')

'''
api.getHashtagFeed('motivacao')
result = api.LastJson
formatado = pprint.pformat(result['ranked_items'][0]['preview_comments'][0]['media_id'])
print(formatado)
'''
#media_id = 2293818168790860777

api.getMediaLikers(2293818168790860777)
result = api.LastJson
for i in range(999):
    usuarios.append(result['users'][i]['pk'])

'''
for i in usuarios:
    with open ('usuarios.txt', 'a') as arquivo:
        arquivo.writelines(str(i) + '\n')
'''


for i in usuarios:
    api.getUsernameInfo(i)
    result = api.LastJson
    print(result['user']['pk'])