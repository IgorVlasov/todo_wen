from app import bot, dp
from aiogram.types import Message
from config import admin_id, todo, HELP
import time



async def send_to_admin(dp):
    await bot.send_message(chat_id = admin_id, text = "Бот запущен!")

@dp.message_handler(command=["start"])
async def start(message:Message):
    await message.answer("Работает")

@dp.message_handler(command=["add"])
async def add(message:Message):
    await message.answer("Работает")

@dp.message_handler(command=["show"])
async def show(message:Message):
    await message.answer("Работает")

@dp.message_handler(command=["done"])
async def done(message:Message):
    await message.answer("Работает")

@dp.message_handler(command=["help"])
async def help(message:Message):
    await message.answer(HELP)

@dp.message_handler()
async def text(message:Message):
    await message.answer(text = message.text)