from repositories.event_repository import EventRepository
from fastapi import Response, Request

class ListAllEventsUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, response: Response, request: Request):
        # Busca todos os eventos
        events = self.event_repository.list_all_events()
        if not events:
            response.status_code = 404
            return {"status": "error", "message": "Nenhum evento encontrado"}

        response.status_code = 200
        return {"status": "success", "events": events}
