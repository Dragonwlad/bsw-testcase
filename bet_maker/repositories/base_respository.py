from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.models.base_model import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class SqlAlchemyRepository(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType]
):
    def __init__(
            self,
            model: type[ModelType],
            session_factory: Callable[[], AbstractContextManager[AsyncSession]]
    ):
        self._session_factory = session_factory
        self.model = model

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data.dict())
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def get_all(self, **filters) -> list[ModelType]:
        async with self._session_factory() as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            return result.scalars().all()
