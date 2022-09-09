import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5631826916:AAFSDkKUJUEdHudJ2K6MsL51O3XnRXIcfdI'
wikipedia.set_lang('ru')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
24    """
    await message.reply("Добро пожаловать в бот Википедии. Этот бот создал Бахромов Азизбек Жасурбек Углы , ученик Президентской школы 6-'green' класса")




@dp.message_handler()
async def wikicha(message: types.Message):
    try:
        respond=wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid hech narsa topilmadi")
if __name__=='__main__':
    executor.start_polling(dp)



