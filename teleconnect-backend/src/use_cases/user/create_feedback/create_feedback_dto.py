from pydantic import BaseModel, Field

class CreateFeedbackDTO(BaseModel):
    user_name: str = Field(..., description="Nome do cliente")
    message: str = Field(..., description="Mensagem do feedback")
    stars: int = Field(..., ge=1, le=5, description="Quantidade de estrelas (1 a 5)")
