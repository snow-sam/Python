from InstagramAPI import InstagramAPI
import os
import json

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open (arquivo , 'r') as arq_json:
            dicionario = json.load(arq_json)
    else:
            dicionario = {}
    return dicionario

def upload_dic(dicionario,arquivo):
    with open(arquivo ,'a') as arq_json:
        json.dump(dicionario, arq_json)



dic = ler_arquivo('medias.json')



api = InstagramAPI('teste131570', 'samucas5')
api.login()

for key in dic.keys():
    lista = []
    for item in dic[key]:
        media = str(item)
        api.getMediaLikers(media[:-10])
        result = api.LastJson
        print(result.keys())
        if result['user_count'] >= 1000:
            lista.append(media[:-10])
        else:
            print('nao')
    
    dic[key] = lista

upload_dic(dic, 'teste.json')