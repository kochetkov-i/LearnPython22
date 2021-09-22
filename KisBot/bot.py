import logging, json, os, ephem, string
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime


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


def get_planet_name_from_user_input(update):
    user_text = update.message.text
    user_words = user_text.split()
    if len(user_words) != 2: 
        return None
    planet_name = user_words[-1].capitalize()
    return planet_name


def get_constellation_by_planet(update, context):
    logging.info("/planet command called")
    planet_name = get_planet_name_from_user_input(update)
    if planet_name is None:
        update.message.reply_text("Try again bro - your string is wrong")
    try:
        user_planet = getattr(ephem, planet_name)()
    except AttributeError:
        update.message.reply_text("Planet not found in lib")
    user_planet.compute(ephem.now())
    planet_constellation = ephem.constellation(user_planet)
    update.message.reply_text(planet_constellation)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def next_full_moon(update, context):
    user_text = update.message.text.replace('/next_full_moon', '')
    if not user_text:
        update.message.reply_text("Try again bro - your string is empty")
    try:
        input_date = datetime.strptime(user_text, '%Y-%m-%d')
    except ValueError:
        update.message.reply_text("Try again bro - your date is not match YYYY-MM-DD")
        return
    next_full_moon = ephem.next_full_moon(input_date)
    output_next_full_moon =f"Next full moon at: {next_full_moon}"
    update.message.reply_text(output_next_full_moon)


def word_count(update, context):
    user_text = update.message.text.replace('/wordcount', '')
    if not user_text:
        update.message.reply_text("Try again bro - your string is empty")
    else:
        for separator in string.punctuation:
            user_text = user_text.replace(separator, ' ')
        user_words = user_text.split()
        word_count = len(user_words)
        for word in user_words:
            if word.isnumeric():
                word_count -= 1
        output_word_count = f"Count of words in your input is: {word_count}"
        update.message.reply_text(output_word_count)


def get_answer(cities, last_char):
    for city in cities:
        if city[0] == last_char:
            return city
    return


def check_user_city(user_data, user_city):
    last_char = user_data['last_char']
    if not last_char:
        return True
    if user_city[0] == last_char and get_answer(user_data['cities'], last_char):
        return True
    return False


def init_game_city(context):
    context.user_data['cities'] = context.bot_data['cities']
    context.user_data['used_cities'] = []
    context.user_data['last_char'] = ''


def processing_game_step(context, city):
        context.user_data['used_cities'].append(city)
        context.user_data['cities'].remove(city)
        context.user_data['last_char'] = city[-1].upper()


def cities(update, context):
    user_text = update.message.text.replace('/cities', '').strip()
    user_text = user_text.capitalize()

    if not user_text:
        update.message.reply_text("Try again bro - your string is empty")
        return
    
    if 'cities' not in context.user_data:
        init_game_city(context)

    if len(context.user_data['cities']) == 0:
        update.message.reply_text("Sorry bro - game is restarted")
        init_game_city(context)

    if user_text in context.user_data['used_cities']:
        update.message.reply_text("Try again bro - this city is already used")
        return
    
    if user_text not in context.user_data['cities']:
        update.message.reply_text("Try again bro - I don't know this city")
        return
    
    if not check_user_city(context.user_data, user_text):
        update.message.reply_text("Try again bro - you lose")
        init_game_city(context)
        return

    processing_game_step(context, user_text)
    bot_answer = get_answer(context.user_data['cities'], context.user_data['last_char'])

    if not bot_answer:
        update.message.reply_text("Congratulations bro - you won")
        return

    processing_game_step(context, bot_answer)
    update.message.reply_text(bot_answer)
    

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.bot_data['cities'] = ['Москва', 'Арзамас', 'Самара', 'Архангельск']
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation_by_planet))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
