import wikipedia
from aiogram import Bot,Dispatcher,executor,types
wikipedia.set_lang('uz')
API_TOKEN = '5441949759:AAFxEkRBUdTF4B1peuG-v6lUETPSe-1VTqU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer("Salom wikipedia botiga xush kelibsiz!")

@dp.message_handler()
async def echo(message: types.Message):

    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except:

        await message.reply("Bu mavzuga oid maqola topilmadi!")

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)

