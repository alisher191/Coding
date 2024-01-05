import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = 'YOUR_TOKEN'
CHANNEL_URL = 'https://t.me/mytestlight'
CHANNEL_ID = '@mytestlight'
CHAT_ID = '@mytestlightchat'
ADMIN_ID = '574726960'

WORDS = ['javascript', 'java']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btnURLChannel = InlineKeyboardButton(text='Перейти на канал:', url=CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)
channelMenu.insert(btnURLChannel)


def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'


# @dp.message_handler(commands=['test'])
# async def test(message: types.Message):
#     await bot.send_message(message.from_user.id, f'ID: {message.from_user.id}')
@dp.message_handler(content_types=['new_chat_member'])
async def user_joined(message: types.Message):
    await message.answer('Добро пожаловать!\nЧтобы отправлять сообщения подпишитесь', reply_markup=channelMenu)


@dp.message_handler()
async def mess_handler(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        text = message.text.lower()
        for word in WORDS:
            for el in text:
                if word == el:
                    await message.delete()
    else:
        await message.answer("Подпишитесь на канал!", reply_markup=channelMenu)
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
