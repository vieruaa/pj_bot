from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from config import token
from logic import pj_promo_code

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command_pj(message: types.Message):
    kb = [[types.KeyboardButton(text='Жирные вздохи удовольствия')], ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='есть парочка промокодов...'
    )
    photo = open('homer.jpg', 'rb')
    await message.reply_photo(photo, 'Кажется, сегодня у нас будет вечер пиццы..', reply_markup=keyboard)


@dp.message_handler(Text('Жирные вздохи удовольствия'))
async def choose_pj_promo(message: types.Message):
    out_string, count = '', 1
    kb = []
    for p in pj_promo_code():
        out_string += str(count) + '. ' + p + '\n\n'
        kb.append([types.KeyboardButton(text=pj_promo_code()[p])])
        count += 1
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выбери номер'
    )
    await message.reply(out_string, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
