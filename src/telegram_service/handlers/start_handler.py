from telegram_service.clients.client_service import ClientService
import telegram_service.factories as factories
from telegram_service.domain.dtos import Client
from telegram_service.loader import dp
from aiogram.types import Message


@dp.message_handler(commands=["start"])
async def start_handler(message: Message) -> Message:
    client: Client = Client(
        telegram_id=message.from_user.id,
        telegram_username=message.from_user.username,
        telegram_fullname=message.from_user.full_name)

    service: ClientService = factories.get_client_service()
    await service.add_client(client)

    return Message(chat_id=client.telegram_id, text="Hello")

