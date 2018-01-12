from telegram.ext import CommandHandler
from telegram.ext import Updater
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater    = Updater(token='543994048:AAHVQF0as1EzsEeuRwtums6mm3OJsLYAcW8')
dispatcher = updater.dispatcher

# long poll for chat updates

# grab new user name from chat update



def start(bot, update):
  bot.send_message(chat_id = update.message.chat_id, 
                      text = "Welcome person to the Bitnation chat, tell us a bit about yourself. Please also see pinned message for current info and updates.")

start_handler = CommandHandler('start', start)



dispatcher.add_handler(start_handler)

updater.start_polling()