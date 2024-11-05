from datetime import datetime

from pydantic import Field

from bet_maker.models.bet_model import BetStatus
from bet_maker.schemas.base_schema import BaseSchema


class BetBase(BaseSchema):
    event_id: str = Field(..., description='Id события')
    amount: float = Field(..., gt=0, description='Сумма ставки')


class BetCreate(BetBase):
    pass


class BetInfo(BetBase):
    id: int
    status: BetStatus
    created_at: datetime
