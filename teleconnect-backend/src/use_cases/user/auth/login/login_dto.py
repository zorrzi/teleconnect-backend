from pydantic import BaseModel, ConfigDict

class LoginDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    email: str
    password: str
