import requests
import telebot
import os

bot = telebot.TeleBot(os.environ.get('ALL_TRIPLETS_BOT_TOKEN', None))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


# URL = 'https://api.telegram.org/bot' + os.environ['ALL_TRIPLETS_BOT_TOKEN'] + '/'

# def get_updates():
#    url = URL + 'getupdates'
#    response = requests.get(url)
#    return response.json()
#def main():
#   dictionary = get_updates()



#     f 'Той-Той любит пластик. Ммммм хрусть-хрусть.')
