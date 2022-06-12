from google.protobuf.empty_pb2 import Empty


class _Base:
    def SerializeToString(self) -> str: ...
    def FromString(self, s: bytes) -> Empty: ...


class Event(_Base):
    text: str
    media: bytes

    def __init__(self, *, text: str, media: bytes) -> None: ...


class MessageRequest(_Base):
    text: str
    telegram_ids: list[int]

    def __init__(self, *, text: str, telegram_ids: list[int]) -> None: ...

