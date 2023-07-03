from aiogram import types
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from callback_datafactory import TestCallbackData
from db import conn, cur
from keyboard import make_keyboard, make_keyboard_with_cancel, make_keyboard_back
from create_message import create_message
from dispatcher import bot
from chatgpt import *

form_router = Router()


class Form(StatesGroup):
    begin = State()
    end = State()
    base = State()
    facts = State()


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
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="regenerate"
        ),
        reply_markup=make_keyboard(result[0])
    )


async def cancel_callback(call: types.CallbackQuery, callback_data: TestCallbackData, state: FSMContext):

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


async def recover_callback(call: types.CallbackQuery, callback_data: TestCallbackData, state: FSMContext):
    await state.set_state(Form.end)
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


async def custom_text_callback(call: types.CallbackQuery, callback_data: TestCallbackData, state: FSMContext):
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )

    # global
    global result
    result = cur.fetchone()
    global callback_global
    callback_global = callback_data
    global msg
    msg = call

    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="custom"),
        reply_markup=make_keyboard_back(id=result[0])
    )
    await state.set_state(Form.begin)


@form_router.message(Form.begin)
async def begin(message: Message, state: FSMContext):
    cur.execute(
        f"""UPDATE tasks
        SET text_birth = '{message.text}'
        WHERE id = {callback_global.id}
        """
    )
    conn.commit()
    await msg.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=message.text, date=result[4], stage="basic"),
        reply_markup=make_keyboard(id=result[0])
    )
    await message.delete()
    await state.clear()
    return
    # del msg, result, callback_global


# add facts
async def add_facts(call: types.CallbackQuery, callback_data: TestCallbackData, state: FSMContext):
    cur.execute(
        f"""select * from tasks
            where id = {callback_data.id}"""
    )

    # global
    global result
    result = cur.fetchone()
    global callback_global
    callback_global = callback_data
    global msg
    msg = call

    await call.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=result[3], date=result[4], stage="facts"),
        reply_markup=make_keyboard_back(id=result[0])
    )
    await state.set_state(Form.facts)


@form_router.message(Form.facts)
async def begin(message: Message, state: FSMContext):
    comp = chatgpt(name=result[1], date=result[4], facts=message.text)
    print(comp)
    cur.execute(
        f"""UPDATE tasks
        SET text_birth = '{comp}'
        WHERE id = {callback_global.id}
        """
    )
    await msg.message.edit_caption(
        caption=create_message(
            name=result[1], group=result[2], compliment=comp, date=result[4], stage="regenerate_with_facts"),
        reply_markup=make_keyboard(id=result[0])
    )
    await message.delete()
    await state.clear()
