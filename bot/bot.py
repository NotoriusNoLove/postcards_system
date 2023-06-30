import asyncio
from aiogram import Bot, Dispatcher
from config import *
from db.users import *
from dispatcher import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from typing import Union
from tasks import check_and_send, create_task, send_postcard
from handlers import *
from callback_func import form_router, Form
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.strategy import FSMStrategy


async def main():
    create_table()
    register_handlers()
    dp.include_router(form_router)
    # insert_users(r'D:\Projects\postcards_system\bot\db\bir.csv')
    # dp.startup.register(send_postcard)  # create_task
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(create_task, trigger='cron', hour=13,
                      minute=41, start_date=datetime.now())
    scheduler.add_job(check_and_send, trigger='cron', hour=13,
                      minute=42, start_date=datetime.now())
    scheduler.add_job(send_postcard, trigger='cron', hour=13,
                      minute=43, start_date=datetime.now())
    scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
