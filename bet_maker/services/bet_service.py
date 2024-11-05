from fastapi import HTTPException, status

from bet_maker.repositories.bet_repository import bet_repository
from bet_maker.schemas.bet_schemas import BetCreate
from bet_maker.services.line_provider_client import fetch_available_events


async def create_bet(bet: BetCreate) -> BetCreate:
    available_events = await fetch_available_events()

    if not any(event.event_id == bet.event_id for event in available_events):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with ID {bet.event_id} does not exist.",
        )

    new_bet = await bet_repository.create(bet)
    return new_bet
