from aiogram import executor, Bot, Dispatcher, types
import requests, time, logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN="6263842022:AAGYghi5eOSM4JbY5MJvInUdbEvuG_1C53U"
MSG = 'Готовился(ась) ли ты сегодня к экзаменам, {}?'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot = bot)

params = {'format' : 2, 'М' : ''}
url = 'https://wttr.in/Perm'
response = requests.get(url, params=params)


HELP_COMMAND = '''
/help - список всех команд
/start - начать работу с ботом
/weather - прогноз погоды'''


b1 = KeyboardButton('/help')
b2 = KeyboardButton('/weather')
b3 = KeyboardButton('Поделиться номером', request_contact=True)
b4 = KeyboardButton('Отправить моё местоположение', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).row(b3, b4)



@dp.message_handler(commands=['start'])
async def start_handler(mesage: types.Message):
    user_id = mesage.from_user.id
    user_name = mesage.from_user.first_name
    user_full_name = mesage.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await mesage.reply(f'Привет, {user_full_name}! Чтобы узнать список всех команд - нажми на /help.', reply_markup=kb_client)

    for i in range(7):
        time.sleep(60*60*24)
        await bot.send_message(user_id, MSG.format(user_name))

@dp.message_handler(commands = ['help'])
async def help_command(mesage: types.Message):
    await mesage.reply(text=HELP_COMMAND)

@dp.message_handler(commands = ['weather'])
async def current_weather(mesage: types.Message):
    await mesage.answer(response.text)


#def register_handlers_client(dp : Dispatcher):
#    dp.register_message_handler(start_handler, commands=['start'])
#    dp.register_message_handler(help_command, commands=['help'])
#    dp.register_message_handler(current_weather, commands=['weather'])



#register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)