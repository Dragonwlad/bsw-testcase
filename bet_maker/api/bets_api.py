from http.client import HTTPException

from fastapi import APIRouter

from bet_maker.repositories.bet_repository import bet_repository
from bet_maker.schemas.bet_schemas import BetCreate, BetInfo
from bet_maker.services.line_provider_client import fetch_available_events
from bet_maker.services import bet_service

router = APIRouter()


@router.post('/bet', response_model=BetCreate)
async def create_bet(bet: BetCreate) -> BetCreate:
    new_bet = await bet_service.create_bet(bet)
    return new_bet


@router.get('/bets', response_model=list[BetInfo])
async def get_bets() -> list[BetInfo]:
    bets = await bet_repository.get_all()
    return bets


@router.get('/events')
async def get_events():
    return await fetch_available_events()
