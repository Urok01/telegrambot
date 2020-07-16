import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-Ульяновск')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot('1301793333:AAEikh5Vvu3tWkkODnZrnuRTBQKug-yw_lY')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

bot.message_handler(commands=['start'])
def main(message):
        bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text)

bot.message_handler(commands=['help'])
def main(message):
        bot.send_message(message.chat.id, "Напиши /start, чтобы узнать погоду.")

bot.message_handler(content_type=["text"])
def main(message):
        bot.send_message(message.chat.id, "Напиши /help, чтобы узнать подробности")

bot.message_handler(content_type=["command"])
def main(message):
        bot.send_message(message.chat.id, "Неизвестная команда")

if __name__ == '__main__':
    bot.polling(none_stop=True)