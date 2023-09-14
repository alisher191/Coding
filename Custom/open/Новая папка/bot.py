import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = '6247492857:AAFaBWN438hniunIdD-hPs-Hj0WgwceidIg'
ADMIN_ID = '574726960'
CHANNEL_URL = 'https://t.me/mytutorialchannel'
CHANNEL_ID = '@mytutorialchannel'
CHAT_ID = '@mytutorialchannelchat'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
WORDS = ['javastript', 'pyphom']



@dp.message_handler()
async def test(message: types.Message):
    if message.text in WORDS:
        await bot.delete_message(message.chat.id, message.from_user.message_id)


def check_sub(member):
    return member['status'] != 'left'


@dp.message_handler()
async def mess_h(message: types.Message):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        text = message.text.lower()
        for word in WORDS:
            if word == text:
                await message.delete()
        await message.answer('Ссылка: https://www.youtube.com/')
    else:
        await message.answer('Подпишитесь на канал!')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
