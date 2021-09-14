import logging, json, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename="bot.log", level=logging.INFO)

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, "config.json")

with open(path_config_file, 'r') as f:
    config = json.load(f)

API_KEY = config["ApiKey"]
PROXY = {'proxy_url': (config["Proxy"]["url"]),
    'urllib3_proxy_kwargs': {
        'username': config["Proxy"]["username"], 
        'password': config["Proxy"]["password"]}}


def greet_user(update, context):
    print("/start command called")
    update.message.reply_text("Hi bro! You pressed /start, congratulation!")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
