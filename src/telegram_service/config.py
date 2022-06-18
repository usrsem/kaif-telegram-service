import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    clients_service_host: str = os.getenv("KAIF_CLIENT_SERVICE_ADDRESS", "")
    bot_token: str = os.getenv("KAIF_TELEGRAM_SERVICE_BOT_TOKEN", "")
    telegram_service_port: int = int(os.getenv(
                                         "KAIF_TELEGRAM_SERVICE_PORT", ""))
    push_pause: float = float(os.getenv(
                                  "KAIF_TELEGRAM_SERVICE_PUSH_PAUSE", "0.3"))


settings = Settings()

