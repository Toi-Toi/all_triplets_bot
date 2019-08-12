import requests
import telebot

URL = 'https://api.telegram.org/bot' + token + '/'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")





# def get_updates():
#    url = URL + 'getupdates'
#    response = requests.get(url)
#    return response.json()
#def main():
#   dictionary = get_updates()



#     f 'Той-Той любит пластик. Ммммм хрусть-хрусть.')
