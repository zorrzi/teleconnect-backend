from pydantic import BaseModel, ConfigDict
from typing import Literal


class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    email: str
    password: str
    front: Literal["Business", "Engenharia", "Direito"]
    position: Literal["Consultor", "Liderança"]