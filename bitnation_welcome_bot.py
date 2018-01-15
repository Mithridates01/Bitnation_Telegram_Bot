from telegram.ext import CommandHandler,Updater,MessageHandler,Filters
import logging
import os

ENV_TOKEN = os.environ.get('Bitnation_Telegram_Bot_Key')

def main(ENV_TOKEN):
  
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
  updater    = Updater(token=ENV_TOKEN)
  dispatcher = updater.dispatcher
  
  def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, 
                        text = "*******TEST********")
  
  def welcome(bot, update):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
  
    for user in msg.new_chat_members:
      bot.send_message(chat.id, 'Welcome {} to the Bitnation chat, tell us a bit about yourself. Please see the pinned message at the top for current info and updates.'.format(
        user.mention_html() ), parse_mode='HTML')
  
  # start_handler = CommandHandler('start', start)
  # dispatcher.add_handler(start_handler)
  
  dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
  
  
  updater.start_polling()
  
  # Deployment
  # setup 2 AWS EC2 with load balancers

if __name__ == "__main__": main(ENV_TOKEN)