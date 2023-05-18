from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6251690600:AAEFKy8YThihaRe13d1Mp0YQiNTrrpjGPSs')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://www.youtube.com/watch?v=y65BZbNB0YA&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=8')))
    await  message.answer('Привет', reply_markup=markup)

executor.start_polling(dp)
