import asyncio
from aiogram import Bot, Dispatcher
from config import *
from db.users import *
from dispatcher import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from typing import Union
from tasks import check_and_send
from handlers import *
from callback_func import form_router


async def main():
    create_table()
    register_handlers()
    dp.include_router(form_router)
    # insert_users(r'D:\Projects\postcards_system\bot\db\bir.csv')
    dp.startup.register(check_and_send)  # insert_task
    # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # scheduler.add_job(check, trigger='cron', hour=4,
    #                   minute=11, start_date=datetime.now())
    # scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')