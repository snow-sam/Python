from instabot import Bot

bot = Bot()

bot.login(username='teste131570', password='samucas5')
#bot.upload_photo('0.jpg', caption='Teste')

result = bot.get_total_hashtag_medias('motivação')
print(result)
