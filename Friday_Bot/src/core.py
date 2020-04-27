from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN
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
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()