import io

from aiogram.bot.bot import Bot
from aiogram.types.input_file import InputFile
from typing import Protocol


class NotificationService(Protocol):
    async def send_message(self, chat_id: int, text: str) -> None: ...
    async def send_photo(
        self,
        chat_id: int,
        photo: bytes,
        caption: str
    ) -> None: ...


class AiogramNotificationService:
    def __init__(self, bot: Bot) -> None:
        self._bot: Bot = bot

    async def send_message(self, chat_id: int, text: str) -> None:
        await self._bot.send_message(chat_id=chat_id, text=text)

    async def send_photo(
        self,
        chat_id: int,
        photo: bytes,
        caption: str
    ) -> None:

        media_bytes_io = io.BytesIO(photo)
        media_file = InputFile(media_bytes_io)

        await self._bot.send_photo(chat_id=chat_id, photo=media_file,
                                   caption=caption)

