from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='6249144600:AAF0OlQ-uLzpLEuI6voi89II-8ZI_6SS47g')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="FAQ", callback_data="faq")
button2 = InlineKeyboardButton(text="Pay USDT", callback_data="payUsdt")
button3 = InlineKeyboardButton(text="Our Address", callback_data="ourAddress")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True).add(
    "FAQ", "Our Address")


@dp.message_handler(commands=['buttons'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply(
        "This bot created for online gold sells for USDT. At the moment we are trading 1 kg and 1 oz of gold.",
        reply_markup=keyboard1)


@dp.callback_query_handler(text=["faq", "ourAddress", "payUsdt"])
async def random_value(call: types.CallbackQuery):
    if call.data == "faq":
        await call.message.answer(
            "Our company Gold Duty Free aiming to deliver our gold around all over city, At the moment we are looking for partners for further growth. Hamza Ozgezici"
        )
    if call.data == "ourAddress":
        await call.message.answer(
            "Phone: 0312 884 448, Address: Kyrgyzstan, Bishkek.")
    if call.data == "payUsdt":
        await call.message.answer("Please, send your address or geolocation", )
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("Hi! How are you?")
    elif message.text == 'Youtube':
        await message.reply("https://youtube.com/gunthersuper")
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)
