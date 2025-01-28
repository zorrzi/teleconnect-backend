from fastapi import APIRouter, Response, Request
from repositories.event_repository import EventRepository
from use_cases.event.list_all_events.list_all_events_use_case import ListAllEventsUseCase

router = APIRouter()
event_repository = EventRepository()
list_all_events_use_case = ListAllEventsUseCase(event_repository)

@router.get("/events")
def list_all_events(response: Response, request: Request):
    return list_all_events_use_case.execute(response, request)
