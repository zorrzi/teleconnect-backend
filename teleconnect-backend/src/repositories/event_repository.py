from typing import List
from mongoengine import *
from entities.event import Event
from models.event_model import EventModel

class EventRepository:
    def save(self, event: Event) -> None:
        event_model = EventModel()
        event_dict = event.model_dump()

        for k in EventModel.get_normal_fields():
            if k not in event_dict:
                continue
            event_model[k] = event_dict[k]

        event_model.save()

    def get_event_by_id(self, event_id: str) -> dict:
        # Busca o evento pelo ID como string
        event = EventModel.objects(id=event_id).first()
        if not event:
            return None
        event_dict = event.to_mongo().to_dict()
        event_dict["_id"] = str(event_dict["_id"])
        return event_dict

    def list_all_events(self) -> List[dict]:
        events = EventModel.objects()
        return [
            {
                **event.to_mongo().to_dict(),
                "_id": str(event.id)
            }
            for event in events
        ]

    def find_by_id_dict(self, id: str) -> dict:
        event = EventModel.objects(id=id).first()
        if not event:
            return None
        event_dict = event.to_mongo().to_dict()
        event_dict["_id"] = str(event_dict["_id"])
        return event_dict

    def delete_event(self, event_id: str) -> None:
        event = EventModel.objects(id=event_id).first()
        if not event:
            raise ValueError("Evento não encontrado para exclusão.")
        event.delete()

    def update_event(self, event_id: str, updated_fields: dict) -> None:
        event = EventModel.objects(id=event_id).first()
        if not event:
            raise ValueError("Evento não encontrado para atualização.")
        
        for field, value in updated_fields.items():
            setattr(event, field, value)

        event.save()

