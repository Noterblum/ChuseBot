import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import setting

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': setting.PROXY_URL, 'urllib3_proxy_kwargs': {'username': setting.PROXY_USERNAME, 'password': setting.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван запуск. Внимание!')
    update.message.reply_text('Привет. Я явился)')

def talk_to_me(update, context):
    text = update.message.text
    print("Что-то пишут")
    update.message.reply_text(text)

def main():
    mybot = Updater(setting.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot start")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()