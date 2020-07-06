from InstagramAPI import InstagramAPI

api = InstagramAPI('_life.motivation', 'samucas5')
api.login()

user1 = 33657077780
user2 = 7368353173
user3 = 24301578378
listaDeUsers = [user1, user2, user3]


def usertofollow(mediaId):
    usuarios = []
    api.getMediaLikers(mediaId)
    result = api.LastJson
    for i in result['users']:
        usuarios.append(i['pk'])
    for usuario in usuarios:
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(str(usuario) + '\n')

def getmediaId(usuario):
    api.getUserFeed(user3)
    result = api.LastJson
    tamanho = len(result['items'])
    for i in range(int(tamanho)):
        with open ('mediaids.txt', 'a') as arquivo:
            arquivo.write(str(result['items'][i]['caption']['media_id']) + '\n')
    return
def getlikenumbers(mediaid):
    api.getMediaLikers(mediaid)
    result = api.LastJson
    print(result['user_count'])
    return

with open('mediaids.txt', 'r') as f:
    medias = [line.strip() for line in f]

for media in medias:
    usertofollow(media)