import asyncio
import requests
from configparser import ConfigParser

from aiogram import Bot, Dispatcher, types

(config := ConfigParser()).read('config.ini', encoding='UTF-8')
dp = Dispatcher()
bot = Bot(token=config['SECURITY']['TOKEN'])


@dp.message()
async def main_handler(message: types.Message):
    print(message.chat.id)
    if not (message.chat.type == 'private'):
        return

    if message.text and message.text != '/start':
        await bot.send_message(config['SECURITY']['FORWARD_CHAT'], message.text)

    elif message.photo:
        await bot.send_photo(config['SECURITY']['FORWARD_CHAT'], photo=types.BufferedInputFile(file=requests.get(
            f'https://api.telegram.org/file/bot{config["SECURITY"]["TOKEN"]}/'
            f'{(await bot.get_file(message.photo[-1].file_id)).file_path}').content,
                                                                                               filename='lambda321'),
                             caption=message.caption if message.caption else None)
    elif message.video:
        await bot.send_video(config['SECURITY']['FORWARD_CHAT'], video=types.BufferedInputFile(file=requests.get(
            f'https://api.telegram.org/file/bot{config["SECURITY"]["TOKEN"]}/'
            f'{(await bot.get_file(message.video.file_id)).file_path}').content,
                                                                                               filename='lambda321'),
                             caption=message.caption if message.caption else None)

    elif message.voice:
        await bot.send_voice(config['SECURITY']['FORWARD_CHAT'], voice=types.BufferedInputFile(file=requests.get(
            f'https://api.telegram.org/file/bot{config["SECURITY"]["TOKEN"]}/'
            f'{(await bot.get_file(message.voice.file_id)).file_path}').content, filename='lambda321'))

    elif message.document:
        await bot.send_document(config['SECURITY']['FORWARD_CHAT'], document=types.BufferedInputFile(file=requests.get(
            f'https://api.telegram.org/file/bot{config["SECURITY"]["TOKEN"]}/'
            f'{(await bot.get_file(message.document.file_id)).file_path}').content, filename='lambda321'),
                                caption=message.caption if message.caption else None)

    elif message.sticker:
        await bot.send_sticker(config['SECURITY']['FORWARD_CHAT'],
                               sticker=types.BufferedInputFile(file=requests.get(
                                   f'https://api.telegram.org/file/bot{config["SECURITY"]["TOKEN"]}/'
                                   f'{(await bot.get_file(message.sticker.file_id)).file_path}').content,
                                                               filename='lambda321'))


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
