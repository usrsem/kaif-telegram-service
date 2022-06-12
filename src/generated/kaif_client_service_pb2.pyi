from typing import Optional
from google.protobuf.empty_pb2 import Empty


class _Base:
    def SerializeToString(self) -> str: ...
    def FromString(self, s: bytes) -> Empty: ...


class Client(_Base):
    telegram_id: int
    telegram_username: Optional[str]
    telegram_fullname: str

    def __init__(self, *, telegram_id: int, telegram_username: Optional[str],
                 telegram_fullname: str) -> None: ...


class ClientRequest(_Base):
    telegram_id: int

    def __init__(self, *, telegram_id: int) -> None: ...

