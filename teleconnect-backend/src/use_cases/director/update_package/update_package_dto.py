from pydantic import BaseModel, Field
from typing import Literal, Optional

class UpdatePackageDTO(BaseModel):
    mobile_service: Optional[Literal["Pré-pago", "Pós-pago"]] = Field(None, description="Tipo de serviço móvel")
    mobile_service_amount: Optional[float] = Field(None, description="Valor para o serviço móvel")
    fiber: Optional[Literal["Básico", "Intermediário", "Família"]] = Field(None, description="Tipo de fibra")
    fiber_amount: Optional[float] = Field(None, description="Valor para o serviço de fibra")
    streaming_partnership: Optional[Literal["GloboPlay", "Premiere"]] = Field(None, description="Parceria com streaming")
    fixed_phone: Optional[bool] = Field(None, description="Telefone fixo incluído no pacote")
    price: Optional[float] = Field(None, description="Preço total do pacote")
    is_b2b: Optional[bool] = Field(None, description="Indica se o pacote é para B2B ou B2C")
