from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram import types
from callback_datafactory import TestCallbackData
from db import conn, cur
from create_message import create_message


def make_keyboard(id, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Перегенерировать", callback_data=TestCallbackData(id=id, event='reg').pack()),
            InlineKeyboardButton(text="❌ Отменить",
                                 callback_data=TestCallbackData(id=id, event='cancel').pack())
        ],
        [InlineKeyboardButton(
            text="✏️ Свой текст", callback_data=TestCallbackData(id=id, event='custom_text').pack())]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def make_keyboard_with_cancel(id, **kwargs):
    buttons = [
        [InlineKeyboardButton(
            text="✅ Восстановить", callback_data=TestCallbackData(id=id, event='recover').pack())]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def make_keyboard_back(id, **kwargs):
    buttons = [
        [InlineKeyboardButton(
            text="⬅ Назад", callback_data=TestCallbackData(id=id, event='recover', **kwargs).pack())]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
