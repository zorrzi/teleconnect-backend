from pydantic import BaseModel, Field
from typing import Literal, Optional

class Package(BaseModel):
    _id: Optional[str]  # O ID será opcional para ser preenchido automaticamente pelo banco
    mobile_service: Literal["Pré-pago", "Pós-pago"] = Field(..., description="Tipo de serviço móvel")
    mobile_service_amount: Optional[float] = Field(None, description="Valor para o serviço móvel")
    fiber: Literal["Básico", "Intermediário", "Família"] = Field(..., description="Tipo de fibra")
    fiber_amount: Optional[float] = Field(None, description="Valor para o serviço de fibra")
    streaming_partnership: Literal["GloboPlay", "Premiere"] = Field(..., description="Parceria com streaming")
    fixed_phone: bool = Field(..., description="Telefone fixo incluído no pacote")
    price: float = Field(..., description="Preço total do pacote")
    is_b2b: bool = Field(..., description="Define se o pacote é para empresas (B2B)")
