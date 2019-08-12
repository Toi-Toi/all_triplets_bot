import requests
import telebot
import os

bot = telebot.TeleBot(os.environ.get('ALL_TRIPLETS_BOT_TOKEN', None))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")




# URL = 'https://api.telegram.org/bot' + os.environ['ALL_TRIPLETS_BOT_TOKEN'] + '/'

# def get_updates():
#    url = URL + 'getupdates'
#    response = requests.get(url)
#    return response.json()
#def main():
#   dictionary = get_updates()



#     f 'Той-Той любит пластик. Ммммм хрусть-хрусть.')
