from dataclasses import dataclass
from typing import Optional


@dataclass
class Client:
    telegram_id: int
    telegram_username: Optional[str]
    telegram_fullname: str


@dataclass
class Event:
    text: str
    media: bytes


@dataclass
class MessageRequest:
    text: str
    telegram_ids: list[int]

