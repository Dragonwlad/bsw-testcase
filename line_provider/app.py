import decimal
import enum
import time

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

from event_publisher import publish_event


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(BaseModel):
    event_id: str
    coefficient: decimal.Decimal | None = None
    deadline: int | None = None
    state: EventState | None = None


events: dict[str, Event] = {
    '1': Event(event_id='1', coefficient=1.2, deadline=int(time.time()) + 600, state=EventState.NEW),
    '2': Event(event_id='2', coefficient=1.15, deadline=int(time.time()) + 60, state=EventState.NEW),
    '3': Event(event_id='3', coefficient=1.67, deadline=int(time.time()) + 90, state=EventState.NEW)
}

app = FastAPI()


@app.put('/event')
async def create_or_update_event(event: Event):
    is_status_update = False
    if event.event_id in events:
        current_event = events[event.event_id]
        if current_event.state != event.state:
            is_status_update = True

    events[event.event_id] = event

    if is_status_update:
        event_data = {
            "event_id": event.event_id,
            "status": event.state.value
        }
        await publish_event(event_data)
    return events[event.event_id]


@app.get('/event/{event_id}')
async def get_event(event_id: str = Path(...)):
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@app.get('/events')
async def get_events() -> list[Event]:
    return list(e for e in events.values() if time.time() < e.deadline)

