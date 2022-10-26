import telebot
from telebot import types
# Загружаем файл для кнопки 1
f = open('data/bt1.txt', 'r', encoding='UTF-8')
text_bt1 = f.read().split('\n')
f.close()
# Загружаем файл для кнопки 2
f = open('data/bt2.txt', 'r', encoding='UTF-8')
text_bt2 = f.read().split('\n')
f.close()
# Загружаем файл для кнопки 3
f = open('data/bt3.txt', 'r', encoding='UTF-8')
text_bt3 = f.read().split('\n')
f.close()
# Загружаем файл для кнопки 4
f = open('data/bt4.txt', 'r', encoding='UTF-8')
text_bt4 = f.read().split('\n')
f.close()
# Загружаем файл для кнопки 5
f = open('data/bt5.txt', 'r', encoding='UTF-8')
text_bt5 = f.read().split('\n')
f.close()
bot = telebot.TeleBot('____')
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Что такое IT?")
        item2 = types.KeyboardButton("Группа в ВК")
        item3 = types.KeyboardButton("Сайт учреждения")
        item4 = types.KeyboardButton("Расписание занятий")
        item5 = types.KeyboardButton("Контакты наставников")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Нажми: \nЧто такое IT? Чтобы узнать больше про сферу.\n Группа в ВК — чтобы получить ссылку на группу ВК. \n Сайт учреждения - чтобы получить ссылку на сайт. \n Расписание занятий - чтобы узнать, какая группа подойдет тебе.\n Контакты наставников - узнать, кто ведет занятия в IT-квантуме.',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Что такое IT?' :
            answer = text_bt1
    elif message.text.strip() == 'Группа в ВК':
            answer = text_bt2
    elif message.text.strip() == 'Сайт учреждения':
        answer = text_bt3
    elif message.text.strip() == 'Расписание занятий':
        answer = text_bt4
    elif message.text.strip() == 'Контакты наставников':
        answer = text_bt5
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)