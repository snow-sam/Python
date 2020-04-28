from instabot import Bot
import json, os

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open (arquivo , 'r') as arq_json:
            dicionario = json.load(arq_json)
    else:
            dicionario = {}
    return dicionario


users = [5583451640, 1393607350, 4268312928, 3102557008, 7008520241]
bot = Bot()

dic = ler_arquivo('medias.json')

bot.login(username='teste131570', password='samucas5')
bot.download_photo(2295487722837726510)



#get_media_likers
#get_link_from_media_id

