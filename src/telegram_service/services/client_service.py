import grpc
import telegram_service.mappers as mappers
from google.protobuf.empty_pb2 import Empty
from generated.kaif_client_service_pb2 import ClientRequest
from generated.kaif_client_service_pb2_grpc import ClientServiceStub
from telegram_service.domain.dtos import Client
from telegram_service.loader import log
from typing import Optional, Protocol



class ClientService(Protocol):
    async def add_client(self, client: Client) -> None: ...
    async def get_client(self, telegram_id: int) -> Optional[Client]: ...
    async def get_all_clients(self) -> list[Client]: ...


class GrpcClientService:
    def __init__(self, clients_service_host: str) -> None:
        self._host: str = clients_service_host
        self._stub: ClientServiceStub
        log.debug(f"{self.__class__.__name__} created")

    @staticmethod
    def update_stub(func):
        async def inner(self, *args, **kwargs):
            with grpc.insecure_channel(self._host) as channel:
                self._stub = ClientServiceStub(channel)
                return await func(self, *args, **kwargs)

        return inner
            

    @update_stub
    async def add_client(self, client: Client) -> None:
        log.debug(f"Adding {client=}")
        client_request = mappers.client_dto_to_message(client)
        return self._stub.AddClient(client_request)

    @update_stub
    async def get_client(self, telegram_id: int) -> Optional[Client]:
        log.debug(f"Getting client with {telegram_id=}")
        client_request = ClientRequest(telegram_id=telegram_id)
        client_response = self._stub.GetClient(client_request)
        return mappers.client_message_to_dto(client_response)

    @update_stub
    async def get_all_clients(self) -> list[Client]:
        log.debug(f"Getting all clients")
        return [
            mappers.client_message_to_dto(c)
            for c in self._stub.GetAllClients(Empty())
        ]

