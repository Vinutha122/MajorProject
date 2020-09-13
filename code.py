!pip3 install adafruit.io
from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data
username = "Vinutha122"                   #change the username
code = "aio_iMsr35NzUG9MKgQGIPA2nPHbVPz4"  #change the key
aio = Client(username,code)

!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=1)
    value_send = aio.create_data('lightbot',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('lit',value)

u = Updater('1149440840:AAEQaJBQjgcA3OnQxA3-x7kZQjuoxYqtBAQ')  #change the token
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
