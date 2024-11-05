from sqlalchemy import update

from bet_maker.core.db.connector import db_connector
from bet_maker.models.bet_model import BetModel, BetStatus
from bet_maker.schemas.event_schema import EventState


async def update_bets_status(event_id: str, new_status: int) -> None:
    async with db_connector.get_db_session() as session:
        event_state = EventState(new_status)

        if event_state == EventState.FINISHED_WIN:
            bet_status: BetStatus = BetStatus.WON
        elif event_state == EventState.FINISHED_LOSE:
            bet_status = BetStatus.LOST
        else:
            bet_status = BetStatus.PENDING

        await session.execute(
            update(BetModel)
            .where(BetModel.event_id == event_id)
            .values(status=bet_status)
        )
        await session.commit()
