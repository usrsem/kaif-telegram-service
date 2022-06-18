import asyncio
from typing import Protocol

from telegram_service.domain.dtos import Event, MessageRequest
from telegram_service.services.client_service import ClientService
from telegram_service.services.notification_service import NotificationService
from telegram_service.config import settings


class TelegramService(Protocol):
    async def send_event(self, event: Event) -> None: ...
    async def send_message(self, message_request: MessageRequest) -> None: ...


class AiogramTelegramService:
    def __init__(
        self,
        notification_service: NotificationService,
        client_service: ClientService,
        push_pause: float = settings.push_pause
    ) -> None:

        self._notification_service: NotificationService = notification_service
        self._client_service: ClientService = client_service
        self._snooze_time: float = push_pause

    async def send_event(self, event: Event) -> None:
        clients_generator = await self._client_service.get_all_clients()
        for client in clients_generator:
            await self._notification_service.send_photo(
                client.telegram_id, event.media, event.text)
            await asyncio.sleep(self._snooze_time)
        
        
    async def send_message(self, message_request: MessageRequest) -> None:
        for id in message_request.telegram_ids:
            await self._notification_service.send_message(
                id, message_request.text)
            await asyncio.sleep(self._snooze_time)

