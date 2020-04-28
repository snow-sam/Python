from InstagramAPI import InstagramAPI

def usertofollow(mediaId):
    api = InstagramAPI('teste131570', 'samucas5')
    api.login()
    usuarios = []


    api.getMediaLikers(mediaId)
    result = api.LastJson

    for i in result['users']:
        usuarios.append(i['pk'])


    print(usuarios)
    for usuario in usuarios:
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(str(usuario) + '\n')
            
api = InstagramAPI('teste131570', 'samucas5')
api.login()
api.mediaInfo(2296896618743594286_7008520241)
result = api.LastJson
print(result)