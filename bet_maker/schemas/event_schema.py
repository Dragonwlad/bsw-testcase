import decimal
import enum

from bet_maker.schemas.base_schema import BaseSchema


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(BaseSchema):
    event_id: str
    coefficient: decimal.Decimal | None = None
    deadline: int | None = None
    state: EventState | None = None

    class Config:
        orm_mode = True
        use_enum_values = True
