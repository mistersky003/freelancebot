import telebot

bot = telebot.TeleBot("5296631435:AAHeX2kTqM1FtpKpzQ1LoUoHv9al5mKiqa4")

@bot.message_handler(commands=['start'])
def send(message):
	bot.reply_to(message, "Howdy, how are you doing?")



if __name__ == '__main__':
    bot.infinity_polling()

