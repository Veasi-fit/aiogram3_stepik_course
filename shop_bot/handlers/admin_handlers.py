from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message(Command(commands=['admin']))
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['/admin'])
