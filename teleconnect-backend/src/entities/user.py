from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    cpf: str
    phone: str
    email: str
    password: str
    name: str
    packages: Optional[List[str]] = []  # Lista de IDs de pacotes adquiridos
