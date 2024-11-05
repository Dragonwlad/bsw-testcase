from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.core.db.connector import db_connector
from bet_maker.models.bet_model import BetModel
from bet_maker.repositories.base_respository import SqlAlchemyRepository
from bet_maker.schemas.bet_schemas import BetCreate, BetInfo


class BetRepository(SqlAlchemyRepository[BetModel, BetInfo, BetCreate]):
    def __init__(
            self,
            session_factory: Callable[[], AbstractContextManager[AsyncSession]]
    ):
        super().__init__(BetModel, session_factory)


bet_repository = BetRepository(session_factory=db_connector.get_db_session)
