import json
import os

import aio_pika
from aio_pika import Message
from dotenv import load_dotenv
from typing import Any


load_dotenv()
QUEUE_URL = os.getenv('QUEUE_URL', default=None)


async def publish_event(event_data: dict[str, Any]):
    """Отправляет сообщение о событии в RabbitMQ."""
    connection = await aio_pika.connect_robust(QUEUE_URL)
    async with connection:
        channel = await connection.channel()

        await channel.declare_queue("events", durable=True)

        message = Message(body=json.dumps(event_data).encode())
        await channel.default_exchange.publish(message, routing_key="events")
