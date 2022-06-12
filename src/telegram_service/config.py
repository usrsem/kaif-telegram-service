import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str = os.getenv("KAIF_TELEGRAM_SERVICE_BOT_TOKEN", "")
    clients_service_host: str = os.getenv("KAIF_CLIENT_SERVICE_ADDRESS", "")
    telegram_service_port: str = os.getenv("KAIF_TELEGRAM_SERVICE_PORT", "")


settings = Settings()

