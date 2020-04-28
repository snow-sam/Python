from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import requests
from conf.settings import TELEGRAM_TOKEN
from os import path


def start(bot, update):
    response_message = "Bem-Vindo S2"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def change(bot, update, args):
    filepath = path.relpath('/home/samsnow/Python/Python/Instagram Project/state.txt')
    with open(filepath, 'w') as arquivo:
        arquivo.write(str(args[0]))
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Feito'
    )

def getbtc(bot, update):
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"from_currency":"BTC","function":"CURRENCY_EXCHANGE_RATE","to_currency":"BRL"}
    headers = {'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",'x-rapidapi-key': "43c9e97d3amshf5f23657734ed50p130a9djsn49d7e7deadc0"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    texto = response.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=texto
    )

def unknown(bot, update):
    response_message = "Comando Invalido"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('change', change, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('getbtc', getbtc)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()