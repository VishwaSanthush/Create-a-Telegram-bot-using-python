from telegram import *
from telegram import update
from telegram.ext import *
from telegram.ext import updater
from telegram.ext import dispatcher
from telegram.ext import commandhandler
from telegram.ext import callbackcontext

bot = Bot("")
#print(bot.get_me())
update=Updater("",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:update,context:CallbackContext):
   bot.send_message(
      chat_id=update.effective_chat.id,
      text="Hi Iam Santhush"
   )
start_value=CommandHandler('start',test_function)

dispatcher.add_handler(start_value)

updater.start_polling()


#Firstly run cmd as administrator after type ( pip install python-telegram-bot  ).
   