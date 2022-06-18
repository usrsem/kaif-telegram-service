import grpc
import telegram_service.factories as factories
from aiogram.types import Message
from telegram_service.services.client_service import ClientService
from telegram_service.domain.dtos import Client
from telegram_service.loader import dp, log


@dp.message_handler(commands=["start"])
async def start_handler(message: Message) -> None:
    log.debug(f"Getting start {message=}")

    client: Client = Client(
        telegram_id=message.from_user.id,
        telegram_username=message.from_user.username,
        telegram_fullname=message.from_user.full_name)

    service: ClientService = factories.get_client_service()

    # FIXME: Start sending exception about created client
    # from server, don't catch UNKNOWN
    try:
        await service.add_client(client)
        await message.reply(text="Hello")
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNKNOWN: # type: ignore
            log.warning(f"Client already in db, {e=}")
        else:
            raise e


