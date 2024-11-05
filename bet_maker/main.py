import time
from contextlib import asynccontextmanager

from fastapi import FastAPI

from bet_maker.api import bets_api
from bet_maker.core.db.connector import db_connector
from bet_maker.models.base_model import Base
from bet_maker.services.event_listener import start_event_listener


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_connector.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    time.sleep(5)
    await start_event_listener()

    try:
        yield
    finally:
        await db_connector.engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(bets_api.router)
