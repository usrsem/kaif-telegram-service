from google.protobuf.empty_pb2 import Empty
import pytest
from generated.telegram_service_pb2 import Event
from telegram_service import factories

from telegram_service.web.grpc_telegram_service import GrpcTelegramService


@pytest.fixture
def service() -> GrpcTelegramService:
    return factories.get_grpc_telegram_serivce()


async def test_send_new_event(service):
    # with open("tests/integration/img.png", "rb") as img:
    #     b = bytes(img.read())

    # event = Event(text="some text", media=b)
    # result = await service.SendNewEvent(event, None)
    # assert type(result) == Empty
    pass


async def test_send_message(service):
    pass

