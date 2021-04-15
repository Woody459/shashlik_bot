import telebot

TOKEN = '1718326634:AAEaglCNacaZbtmrYn49cAd8LvJQLa7frG0'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


bot.polling(none_stop=True, interval=0)
