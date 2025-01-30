from pydantic import BaseModel
from typing import List
from pydantic.fields import Field

class RegisterDTO(BaseModel):

    cpf: str
    phone: str
    email: str
    password: str
    name: str
    packages: List[str] = Field(default_factory=list)
