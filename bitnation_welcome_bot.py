from telegram.ext import CommandHandler,Updater,MessageHandler,Filters
import telegram.error
import logging
import sys
import os

ENV_TOKEN = os.environ.get('Bitnation_Telegram_Bot_Key')

def main(ENV_TOKEN):
  
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      filename='bot.logs',
                      filemode='a')
  
  updater    = Updater(token=ENV_TOKEN)
  dispatcher = updater.dispatcher
  
  def test(bot, update):
    bot.send_message(chat_id = update.message.chat_id, 
                        text = "*******TEST********")
  
  def welcome(bot, update):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
  
    for user in msg.new_chat_members:
      bot.send_message(chat.id, 'Welcome {} to the Bitnation chat, tell us a bit about yourself. Please see the pinned message at the top for current info and updates.'.format(
        user.mention_html() ), parse_mode='HTML')
  
  test_handler = CommandHandler('test666', test)
  dispatcher.add_handler(test_handler)
  
  dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
  
  
  updater.start_polling(timeout=400)
  
  # Deployment
  # setup 2 AWS EC2 with load balancers
  sys.exit()
if __name__ == "__main__": main(ENV_TOKEN)