import json

from aio_pika import connect_robust, IncomingMessage

from bet_maker.services.update_bet import update_bets_status
from core.config.config import settings


async def process_event_message(message: IncomingMessage):
    """Обрабатывает сообщение из очереди RabbitMQ и
    обновляет статусы ставок."""
    async with message.process():
        event_data = json.loads(message.body)
        event_id = event_data.get("event_id")
        new_status = event_data.get("status")

        if event_id and new_status:
            await update_bets_status(event_id, new_status)


async def start_event_listener():
    """Запускает подключение к очереди RabbitMQ для получения событий."""
    connection = await connect_robust(settings.QUEUE_URL)
    channel = await connection.channel()

    queue = await channel.declare_queue("events", durable=True)

    await queue.consume(process_event_message)
    print("Прослушивание очереди RabbitMQ началось.")
