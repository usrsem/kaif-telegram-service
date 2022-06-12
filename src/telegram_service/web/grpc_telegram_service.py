from google.protobuf.empty_pb2 import Empty
from generated import telegram_service_pb2_grpc, telegram_service_pb2
from telegram_service import mappers
from telegram_service.services.telegram_service import TelegramService


class GrpcTelegramService(telegram_service_pb2_grpc.TelegramService):
    def __init__(self, service: TelegramService) -> None:
        self._service: TelegramService = service

    async def SendNewEvent(
        self,
        event: telegram_service_pb2.Event,
        _
    ) -> Empty:
        event_dto = mappers.event_message_to_dto(event)
        await self._service.send_event(event_dto)
        return Empty()

    async def SendMessage(
        self,
        request: telegram_service_pb2.MessageRequest,
        _
    ) -> Empty:
        request_dto = mappers.message_request_message_to_dto()
        await self._service.send_message(request_dto)
        return Empty()
