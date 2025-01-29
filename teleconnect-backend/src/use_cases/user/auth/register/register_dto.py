from pydantic import BaseModel

class RegisterDTO(BaseModel):

    cpf: str
    phone: str
    email: str
    password: str
    name: str
