from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine
)

from bet_maker.core.config.config import settings


class DatabaseConnector:
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.DB_URL,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False
        )

    @asynccontextmanager
    async def get_db_session(self) -> AsyncIterator[AsyncSession]:
        session: AsyncSession = self.session_factory()
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()


db_connector = DatabaseConnector()
