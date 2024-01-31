import telebot

bot = telebot.TeleBot('6901567208:AAEm0BlKPWp_ty9XzN1BKpYasPsgcvhXx_0')


@bot.message_handler(commands=['start'])
def main(msg):
    bot.send_message(msg.chat.id, 'привет,испытай удачу и посмотри налево')
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    but1 = telebot.types.InlineKeyboardButton('Первая', callback_data='first')
    but2 = telebot.types.InlineKeyboardButton('Вторая', callback_data='Second')
    markup.add(but1, but2)
    bot.send_message(msg.chat.id, 'выбери кнопку ниже', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'first':
            bot.send_message(call.message.chat.id, 'мимо')
        if call.data == 'Second':
            bot.send_message(call.message.chat.id, 'молодец,попал')


bot.infinity_polling()
