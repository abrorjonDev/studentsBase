import environ
from django.http import HttpResponse
import telebot
env = environ.Env()

TOKEN = env('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


def webhook(request):
    if request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode("utf-8"))])
        return HttpResponse('')
    else:
        return HttpResponse('Invalid request')


@bot.message_handler(commands=['start', 'help', 'my-forms'])
def commands(message):
    ...


@bot.message_handler()
def echo_bot(message):
    bot.send_message(chat_id=message.chat.id, text=message.text)