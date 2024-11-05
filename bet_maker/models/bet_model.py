import enum

from sqlalchemy import String, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column

from bet_maker.models.base_model import Base


class BetStatus(enum.Enum):
    PENDING = 'pending'
    WON = 'won'
    LOST = 'lost'


class BetModel(Base):
    event_id: Mapped[str] = mapped_column(String, index=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[BetStatus] = mapped_column(
        Enum(BetStatus),
        default=BetStatus.PENDING,
        nullable=False
    )
