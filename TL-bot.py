import requests
from bs4 import BeautifulSoup
import random
import telebot

token = '5982867252:AAH2DnF_M7T8HQU1gCINe0gML7XtEeaEde4'
bot = telebot.TeleBot(token)
while True:
    try:
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            welcome_txt = '''
            Добро пожаловать!
            список команд: /start /help /img
            /alb /rsong 
            '''
            bot.send_message(message.chat.id, welcome_txt)

        @bot.message_handler(commands=['alb'])
        def send_alboum(message):
            global k
            for i in range(len(songs)):
                alb = open(str(songs[k]), 'rb')
                k += 1
                bot.send_audio(message.chat.id, alb)

        @bot.message_handler(commands=['rsong'], content_types='text')
        def send_random_song(message):
            ransong = open(random.choice(songs), 'rb')
            bot.send_audio(message.chat.id, ransong)

        @bot.message_handler(commands=['img'])
        def send_img(message):
            img = open('Katanekk.jpg', 'rb')
            bot.send_photo(message.chat.id, img)

        @bot.message_handler(content_types='text')
        def message_reply(message):
            if 'новогодний трап' in message.text:
                song = open('x-mas_TRAP.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'без мелодии' in message.text:
                song = open('без мелодии.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'беспорядок' in message.text:
                song = open('беспорядок.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'такие дела' in message.text:
                song = open('такие дела.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'блаженство' in message.text:
                song = open('блаженство.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'винлайн' in message.text:
                song = open('винлайн.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            if 'эхо' in message.text:
                song = open('эхо.m4a', 'rb')
                bot.send_audio(message.chat.id, song)
            else:
                bot.send_message(message.chat.id, message.text)
    finally:
        0

k = 0
songs = ["без мелодии.m4a", "беспорядок.m4a", "такие дела.m4a", "блаженство.m4a", "винлайн.m4a", "эхо.m4a"]
bot.polling()
