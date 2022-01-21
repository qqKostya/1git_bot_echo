import logging
import os

from aiogram import Bot, Dispatcher, types

# log
logging.basicConfig(level=logging.INFO)


# handlers
async def start(message: types.Message):
    await message.reply('Привет, {0}!'.format(message.from_user.first_name))


async def echo(message: types.Message):
    await message.answer(message.text)


# Selectel Lambda funcs
async def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(echo)


async def process_event(update, dp: Dispatcher):
    Bot.set_current(dp.bot)
    await dp.process_update(update)


# Selectel serverless entry point
async def main(**kwargs):
    bot = Bot(os.environ.get("TOKEN"))
    dp = Dispatcher(bot)

    await register_handlers(dp)

    update = types.Update.to_object(kwargs)
    await process_event(update, dp)

    return 'ok'
