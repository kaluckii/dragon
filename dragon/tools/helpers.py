from datetime import datetime
from typing import List, Optional, Tuple

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytz import timezone


def escape(text: str, skip: Optional[List] = None) -> str:
    """
    Escape special characters in a string for use in Telegram MarkdownV2,
    including (not skipped) the following characters: . - ! ( ) | # + = : _
    """

    for char in [".", "-", "!", "(", ")", "|", "#", "+", "=", ":", "_"]:
        if not skip or char not in skip:
            text = text.replace(char, "\\" + char)

    return text


def build_keyboard(buttons: List[Tuple[str, str]], rows: int = 2) -> InlineKeyboardMarkup:
    """
    Builds an InlineKeyboardMarkup using the given set of buttons and specified
    row configuration. Detects hyperlinks in the provided data and creates url-button.
    """

    builder = InlineKeyboardBuilder()
    for text, callback in buttons:
        if not "http" in callback:
            builder.button(text=text, callback_data=callback)

        else:
            builder.button(text=text, url=callback)

    builder.adjust(rows, repeat=True)
    return builder.as_markup()


def use_time(tz: Optional[str] = "Europe/Moscow") -> str:
    """
    Gets the current time in the provided timezone formatted as "HH:MM:SS".
    """

    return datetime.now(timezone(tz)).strftime("%H:%M:%S")

