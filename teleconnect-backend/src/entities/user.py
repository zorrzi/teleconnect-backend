from pydantic import BaseModel, EmailStr

class User(BaseModel):
    cpf: str
    phone: str
    email: EmailStr
    password: str
    name: str