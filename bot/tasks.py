from config import *
from db.users import *
from dispatcher import dp, bot
from keyboard import make_keyboard
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import FSInputFile
import modify
from create_message import create_message


async def create_task():
    if len(users := test()) == 0:
        return
    insert_task(users)


async def send_message_birth(**kwargs):
    text = " ".join((kwargs.get("name").split())[0:2])
    group = kwargs.get("group")
    await bot.send_photo(
        photo=FSInputFile(modify.draw_image(text_img=text, shad=group)),
        chat_id="-1001951834621",
        caption=create_message(stage="basic", **kwargs),
        reply_markup=make_keyboard(**kwargs),
        parse_mode="HTML"

    )


async def check_and_send():  # test (+ INTERVAL '1 day)'
    cur.execute("""
    SELECT *
    FROM tasks
    WHERE TO_CHAR(send_date, 'MM-DD') = TO_CHAR(CURRENT_DATE + INTERVAL '1 day', 'MM-DD')
    """
                )
    result = cur.fetchall()
    if len(result) == 0:
        print("No tasks")
        return
    for item in result:
        await send_message_birth(id=item[0], name=item[1], group=item[2], compliment=item[3], date=item[4])


async def send_postcard():
    cur.execute("""
    SELECT *
    FROM tasks
    WHERE TO_CHAR(send_date, 'MM-DD') = TO_CHAR(CURRENT_DATE  + INTERVAL '1 day', 'MM-DD') and submit = true
    """
                )
    result = cur.fetchall()
    if result is None:
        return
    for item in result:
        await bot.send_photo(
            photo=FSInputFile(modify.draw_image(
                text_img=" ".join((item[1].split())[0:2]), shad=item[2])),
            chat_id=group_id[item[2]],
            caption=item[3],
            parse_mode="HTML"
        )
