import logging
from unicodedata import name

from aiogram import Bot, Dispatcher, executor, types

from exchangerate import info, convertation

API_TOKEN = 'Your Token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(user_id,f"👋 Salom!    {user_name} \nMen Eexchange Rate Bot ==> USD ni UZS convertatsiya bot!\nBuyruqlar /usdkurs kursni bilish, qiymat kiriting va dollarni somdagi qiymatini biling!")
    exrat = info['conversion']
    time  = info['time']
    await message.answer(f"Sana: {time}\nKurs: 🇺🇸 1 USD  🇺🇿 {exrat}  so'mga teng")

async def start(message: types.Message):
    await bot.send_message(message.from_user.id, message.from_user.first_name)

@dp.message_handler(commands=['usdkurs'])
async def send_welcome(message: types.Message):
    exrat = info['conversion']
    time  = info['time']
    await message.answer(f"Sana: {time}\nKurs: 🇺🇸 1 USD  🇺🇿 {exrat}  so'mga teng")

@dp.message_handler()
async def echo(message: types.Message):
    
    try:
      usd = float(message.text)
      sum = convertation(usd)
      await message.answer(f"🇺🇸 {usd}$  dollar \n🇺🇿 {sum} ga teng.")
    except:
      await message.answer("convertatsiya qilish uchun son kiriting")
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
