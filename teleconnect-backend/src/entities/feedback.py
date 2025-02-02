from pydantic import BaseModel, Field
from typing import Optional

class Feedback(BaseModel):
    _id: Optional[str] = None
    user_id: str = Field(..., description="Nome do cliente que fez o feedback")
    feedback_text: str = Field(..., description="Mensagem do feedback")
    stars: int = Field(..., ge=1, le=5, description="Quantidade de estrelas (1 a 5)")
