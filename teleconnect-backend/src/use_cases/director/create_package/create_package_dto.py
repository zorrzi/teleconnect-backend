from pydantic import BaseModel, Field
from typing import Literal, Optional

class CreatePackageDTO(BaseModel):
    mobile_service: Literal["Pré-pago", "Pós-pago"] = Field(..., description="Tipo de serviço móvel")
    mobile_service_amount: Optional[float] = Field(None, description="Valor para o serviço móvel, obrigatório para Pós-pago")
    fiber: Literal["Básico", "Intermediário", "Família"] = Field(..., description="Plano de fibra")
    fiber_amount: Optional[float] = Field(None, description="Valor do plano de fibra, se aplicável")
    streaming_partnership: Literal["GloboPlay", "Premiere"] = Field(..., description="Parceria com plataformas de streaming")
    fixed_phone: bool = Field(..., description="Indica se o pacote possui telefonia fixa")
    price: float = Field(..., gt=0, description="Preço total do pacote")
    is_b2b: bool = Field(..., description="Define se o pacote é para empresas (B2B)")
