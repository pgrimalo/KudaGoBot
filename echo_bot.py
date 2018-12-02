import ast
from cgi import log

import requests
import telebot
import constants1 as constants
from telebot import types
from choice import choice_main, location_search, users_count

sm = u'\U0001F603'
sm1 = u'\U0001F601'
bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.helpAnswer)
    log(message, constants.helpAnswer)


@bot.message_handler(commands=['start', 'Начать'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('/События рядом')
    markup.row('/Все события')
    bot.send_message(message.chat.id, "Выберите категорию", reply_markup=markup)


@bot.message_handler(commands=["События"])
def request_location(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Нам нужно ваше местоположение", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def location(message):
    bot.send_message(message.chat.id, 'Подождите...Ищем события... ')
    lat = (ast.literal_eval(str(message.location))["latitude"])
    lon = (ast.literal_eval(str(message.location))["longitude"])
    big_dick=""
    answer = location_search(lat, lon)
    for d in range(len(answer)):
        if type(answer) == str:
            big_dick = answer
        else:
            try:
                message1 = "\n" + answer[d]["title"] + "\n" + answer[d][
                    "content"] + "\n" + "Начало события: " + \
                           answer[d][
                               "start"] + "\n" + "Конец события: " + answer[d]["end"] + "\n" + answer[d][
                               "url"]
            except KeyError:
                message1 = "\n" + answer[d]["title"] + "\n" + answer[d][
                    "content"] + "\n" + answer[d]["end"] + "\n" + answer[d][
                               "url"]
            big_dick += message1
    bot.send_message(message.chat.id, big_dick)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
    keyboard.add(types.KeyboardButton('/Начать сначала'))
    bot.send_message(message.chat.id, sm + 'Мы всегда рады помочь Вам!', reply_markup=keyboard)


@bot.message_handler(commands=['Все'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('/Квесты', '/Концерты')
    markup.row('/Стендап', '/Фестивали')
    markup.row('/Знания', '/Выставки')
    markup.row('/Ярмарки', '/Дети')
    markup.row('/Постоянные выставки')
    bot.send_message(message.chat.id, constants.startAnswer, reply_markup=markup)
    log(message, constants.startAnswer)


@bot.message_handler(commands=['Квесты'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)

    global text
    text = message.text


@bot.message_handler(commands=['Концерты'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Стендап'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Показать события')
    markup1.add(m1)
    bot.send_message(message.chat.id, 'Данное событие является платным', reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Фестивали'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Ярмарки'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Постоянные'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Выставки'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Знания'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Дети'])
def handle_start(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    m1 = types.KeyboardButton('/Платное')
    m2 = types.KeyboardButton('/Бесплатное')
    m3 = types.KeyboardButton('/Не имеет значения')
    markup1.add(m1, m2, m3)
    bot.send_message(message.chat.id, "Выберите тип события", reply_markup=markup1)
    global text
    text = message.text


@bot.message_handler(commands=['Платное', 'Бесплатное', 'Не', 'Показать'])
def handle_start(message):
    try:
        bot.send_message(message.chat.id, 'Подождите...Ищем события...')
        try:
            dermo = choice_main(text)
        except requests.exceptions.ReadTimeout:
            bot.send_message(message.chat.id,
                             'Превышено время ожидания ответа от KudaGo.com...Попробуйте заново через несколько минут')
        for i in range(len(dermo)):
            mes = "#" + str(i + 1) + "\n" + dermo[i]["title"] + "\n" + " " + dermo[i][
                "content"] + "\n" + "Смотреть больше:" + dermo[i]["url"]

            bot.send_message(message.chat.id, mes)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
        keyboard.add(types.KeyboardButton('/Начать сначала'))
        bot.send_message(message.chat.id, sm + 'Мы всегда рады помочь Вам!', reply_markup=keyboard)
        users_count()


    except NameError:
        bot.send_message(message.chat.id, "Извините!Произошла неизвестная ошибка..." + sm1)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
        keyboard.add(types.KeyboardButton('/Начать сначала'))
        bot.send_message(message.chat.id, 'Попробуйте найти события еще раз', reply_markup=keyboard)
        users_count()


if __name__ == '__main__':
    bot.polling(none_stop=True)
