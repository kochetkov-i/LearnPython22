import logging, json, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem


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
    logging.info("/start command called")
    update.message.reply_text("Hi bro! You pressed /start, congratulation!")


def get_clear_planet(update):
    try:
        user_text = update.message.text
        user_words = user_text.split()
        if len(user_words) != 2: raise ValueError
        planet_name = user_words[-1].capitalize()
        planet_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]
        if planet_name not in planet_list: raise ModuleNotFoundError
        return planet_name
    except ValueError: update.message.reply_text("Try again bro - your string is wrong")
    except ModuleNotFoundError: update.message.reply_text("Planet not found in lib")
    


def get_constellation_by_planet(update, context):
    logging.info("/planet command called")
    planet_name = get_clear_planet(update)
    user_planet = getattr(ephem, planet_name)()
    user_planet.compute(ephem.now())
    planet_constellation = ephem.constellation(user_planet)
    update.message.reply_text(planet_constellation)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation_by_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
