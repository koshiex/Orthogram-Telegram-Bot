import telebot, time, logging, sys
from pyaspeller import YandexSpeller
from telebot import types
from config import TOKEN

def Fixing(message):
    speller = YandexSpeller()
    fixed = speller.spelled(message)
    return fixed


bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    try:
        r = types.InlineQueryResultArticle('1', 'Результат', types.InputTextMessageContent(
            "🤓 Ваабщета правильна: {}".format(Fixing(query.query))), description="Исправление ошибок")
        r2 = types.InlineQueryResultArticle('2', 'Заглушка', 
            types.InputTextMessageContent(
"""Паша Дуров лох, не дает сделать без этой заглушки. 
Сделано kobay9iq. [Мой пустой гитхаб](https://github.com/kobay9iq)""", parse_mode = "Markdown")
            )
        bot.answer_inline_query(query.id, [r, r2])
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