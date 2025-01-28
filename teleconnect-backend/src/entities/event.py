from pydantic import BaseModel
from typing import Optional, List

class Event(BaseModel):
    _id: str
    name: str
    description: Optional[str] = "Evento sem descrição"
    date: str  # Agora a data é uma string no formato YYYY-MM-DD
    location: str
    capacity: int
    start_time: str
    end_time: str
    participants: List[str] = []
