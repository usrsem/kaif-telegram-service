import generated.kaif_client_service_pb2 as client_pb2
import generated.telegram_service_pb2 as telegram_pb2
import telegram_service.domain.dtos as dtos


def client_message_to_dto(c: client_pb2.Client) -> dtos.Client:
    return dtos.Client(
        telegram_id=c.telegram_id,
        telegram_username=c.telegram_username,
        telegram_fullname=c.telegram_fullname)


def client_dto_to_message(c: dtos.Client) -> client_pb2.Client:
    return client_pb2.Client(
        telegram_id=c.telegram_id,
        telegram_username=c.telegram_username,
        telegram_fullname=c.telegram_fullname)


def message_request_message_to_dto(
    m: telegram_pb2.MessageRequest
) -> dtos.MessageRequest:
    return dtos.MessageRequest(
        text=m.text,
        telegram_ids=m.telegram_ids)


def event_message_to_dto(e: telegram_pb2.Event) -> dtos.Event:
    return dtos.Event(
        text=e.text,
        media=e.media )

