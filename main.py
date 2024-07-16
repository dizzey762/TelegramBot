from aiogram import Bot, types, Dispatcher, F
import asyncio
import sqlite3
from aiogram.filters.command import Command

connection = sqlite3.connect('database.db')

connection.close()
API_TOKEN = '6625438911:AAEIf_MvgB8I_cvrYWL_scttQ5mNe-S9CkM'

bot = Bot(token=API_TOKEN)

dp = Dispatcher()

dp.message()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [
        types.KeyboardButton(text ='RPG'),
        types.KeyboardButton(text = 'Slasher'),
        types.KeyboardButton(text='Casual'),
        types.KeyboardButton(text='Sport')
    ],
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder=('Выберите жанр'))
    await message.answer('заебал', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
