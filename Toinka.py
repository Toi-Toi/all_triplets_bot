import telebot
import os

token = os.environ.get('ALL_TRIPLETS_BOT_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")








# Той-Той любит пластик. Ммммм хрусть-хрусть.
#bot.polling()
print(token)
