from aiogram.filters.callback_data import CallbackData


class TestCallbackData(CallbackData, prefix="test"):
    event: str
    id: int
    # group: str
    # date: str
    # compliment: str
