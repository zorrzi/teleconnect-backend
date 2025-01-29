from pydantic import BaseModel, EmailStr

class User(BaseModel):
    cpf: str
    phone: str
    email: str
    password: str
    name: str