import clima_valencia
import variables
import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

def tiempo(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id, text="%s \n %s \n %s \n %s" %clima_valencia.tiempo())


def main():
    updater = Updater(variables.Token)
    updater.dispatcher.add_handler(CommandHandler('tiempo', tiempo))
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()
