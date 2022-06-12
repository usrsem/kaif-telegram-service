import asyncio
import telegram_service.factories as factories
import generated.telegram_service_pb2_grpc as pb2_grpc
import grpc
from telegram_service.loader import log
from telegram_service.config import settings


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_TelegramServiceServicer_to_server(
        factories.get_grpc_telegram_serivce(), server)
    server.add_insecure_port(f"[::]:{settings.telegram_service_port}")
    await server.start()
    await server.wait_for_termination()


def run() -> None:
    log.info("Starting telegram service")
    asyncio.get_event_loop().run_until_complete(serve())


if __name__ == '__main__':
    run()

