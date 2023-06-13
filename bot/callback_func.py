from aiogram import types
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from callback_datafactory import TestCallbackData
from db import conn, cur
from keyboard import make_keyboard, make_keyboard_with_cancel
from create_message import create_message
from dispatcher import bot


async def regeneration_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    # реген текста от гпт
    cur.execute(
        f"""UPDATE tasks
        set text_birth = 'new_regen'
        where id = {callback_data.id}
        """
    )
    conn.commit()
    # получаем уже измененные данные
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )
    result = cur.fetchone()
    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="basic"
        ),
        reply_markup=make_keyboard(result[0])
    )


async def cancel_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    # меняем submit на false
    cur.execute(
        f"""UPDATE tasks
        SET submit = False
        WHERE id = {callback_data.id}
        """
    )
    conn.commit()
    # достаем данные
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )
    result = cur.fetchone()
    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="cancel"),
        reply_markup=make_keyboard_with_cancel(id=result[0])
    )


async def recover_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    # меняем submit на true
    cur.execute(
        f"""UPDATE tasks
        SET submit = True
        WHERE id = {callback_data.id}
        """
    )
    conn.commit()
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )
    result = cur.fetchone()
    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="basic"),
        reply_markup=make_keyboard(id=result[0])
    )

form_router = Router()


class Form(StatesGroup):
    begin = State()
    end = State()


async def custom_text_callback(call: types.CallbackQuery, callback_data: TestCallbackData, state: FSMContext):
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )
    result = cur.fetchone()
    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="custom")
    )
    await state.set_state(Form.begin)


@form_router.message(Form.begin)
async def begin(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Привет')
