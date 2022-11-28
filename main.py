import telebot, time, logging, sys
from pyaspeller import YandexSpeller
from telebot import types
from config import *

def Fixing(message):
    speller = YandexSpeller()
    fixed = speller.spelled(message)
    return fixed


bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    try:
        r = types.InlineQueryResultArticle('1', 'Результат', types.InputTextMessageContent(
            ResultPrefix.format(Fixing(query.query))), 
            description="Исправление ошибок", thumb_url=ResultThumbnail)
        r2 = types.InlineQueryResultArticle('2', 'Автор бота', 
            types.InputTextMessageContent(CreditsText, parse_mode = "Markdown"),
            thumb_url=CreditsThumbnail)
        if CreditsEnabled: bot.answer_inline_query(query.id, [r,r2])
        else: bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)

while True:
    try:
        print("STARTED")
        bot.polling(none_stop=True)
    except: 
      print('bolt')
      logging.error('error: {}'.format(sys.exc_info()[0]))
      time.sleep(5)