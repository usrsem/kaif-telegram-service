from telegram_service.services.notification_service import AiogramNotificationService
from telegram_service.services.telegram_service import AiogramTelegramService
from telegram_service.services.client_service import ClientService, GrpcClientService
from telegram_service.web.grpc_telegram_service import GrpcTelegramService
from telegram_service.loader import bot
from telegram_service.config import settings


def get_client_service() -> ClientService:
    return GrpcClientService(settings.clients_service_host) # type: ignore


def get_grpc_telegram_serivce() -> GrpcTelegramService:
    notification_service = AiogramNotificationService(bot)
    client_service = get_client_service()
    telegram_service = AiogramTelegramService(
        notification_service, client_service)
    return GrpcTelegramService(telegram_service)

