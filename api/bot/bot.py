import telebot
import requests
from telebot import types
base_url = "http://127.0.0.1:8000/api"
bot = telebot.TeleBot("6063559416:AAGB9lk6taq-mUyq3KH9zON0dJU_SQ8KTk4")


markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
markup.add(types.KeyboardButton("Ro'yhatdan o'tish"), types.KeyboardButton("Admin Bilan Bog'lanish"), types.KeyboardButton('Biz haqimizda'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  try:
    text = requests.get(f'{base_url}/info/').json()
    bot.send_message(message.from_user.id, text['text'], reply_markup=markup)
  except Exception as err:
    print(err)
    bot.reply_to(message, "hush kelibsiz!", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
  if message.text == "Biz haqimizda":
    query = requests.get(f'{base_url}/detail/').json()
    text = f"O'quv markazi:\n{query['text']}"
    bot.send_location(message.from_user.id, latitude=query['lat'], longitude=query['lng'], reply_markup=markup)
    bot.send_message(message.from_user.id, text)
  elif message.text == "Ro'yhatdan o'tish":
    query = requests.get(f'{base_url}/science/').json()
    science_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for i in query:
      buttons.append(types.KeyboardButton(f"{i['name']}"))
      if len(buttons) == 2:
        science_markup.add(buttons[0], buttons[1])
        buttons.clear()
    if len(buttons) == 1:
      science_markup.add(buttons[0])
      buttons.clear()
    science_markup.add(types.KeyboardButton("Ortga"))
    bot_message = bot.send_message(message.from_user.id, "O'zingiz o'qimoqchi bo'lgan fanni tanlang!", reply_markup=science_markup)
    bot.register_next_step_handler(bot_message, name_controller)
  else:
    bot.send_contact(message.from_user.id,+998933845384, 'Abduxoliq')
    bot.send_message(message.from_user.id, "+Adminga murojat qilish vaqti(8:00 dan 20:00 gacha):+998933845284,\n+998975806040")

def name_controller(message):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    science = message.text
    bot_message = bot.send_message(message.from_user.id, 'Ismingizni kiriting!', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, last_name_controller, science)

def last_name_controller(message,science):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    name = message.text
    bot_message = bot.send_message(message.from_user.id, 'Familiyangizni kiriting!', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, age_controller, science, name)


def age_controller(message, science, name):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    last_name = message.text
    bot_message = bot.send_message(message.from_user.id, 'Yoshingizni kiriting!', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, phone_controller1, science, name, last_name)



def phone_controller1(message, science, name, last_name):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    age = message.text
    bot_message = bot.send_message(message.from_user.id, 'Telefon kiriting(Masalan: 933125284)!', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, phone_controller2, science, name, last_name, age)


def phone_controller2(message, science, name, last_name, age):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    phone_number1 = message.text
    bot_message = bot.send_message(message.from_user.id, "Qo'shimcha telefon kiriting(Masalan: 999345262)!", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, free_time_controller, science, name, last_name, age, phone_number1)

def free_time_controller(message, science, name, last_name, age, phone_number1):
  if message.text == "Ortga":
    send_welcome(message)
  else:
    phone_number2 = message.text
    bot_message = bot.send_message(message.from_user.id, "Bo'sh vaqtingizni kiriting(12:00,20:00)!", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(bot_message, add_student, science, name, last_name,age, phone_number1, phone_number2)



def add_student(message, science, name, last_name,age, phone_number1,phone_number2):
    if message.text == "Ortga":
      send_welcome(message)
    else:
      phone_number1=phone_number1
      free_time = message.text
      print(science, name, last_name, age, phone_number1,phone_number2, free_time)
      data = {
        "science": science,
        "first_name": name,
        'age': age,
        "last_name": last_name,
        "phone_number1": phone_number1,
        "phone_number2": phone_number2,
        "free_time": free_time,
      }
      query = requests.post(f'{base_url}/add_student', data=data)
      bot.send_message(message.from_user.id,"Siz muvaffaqqiyatli Ro'yhatdan o'tdingiz 👌")



bot.infinity_polling()