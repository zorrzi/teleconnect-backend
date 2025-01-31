from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional


class CreatePackageDTO(BaseModel):
    mobile_service: Optional[Literal["Pré-pago", "Pós-pago"]] = Field(None, description="Tipo de serviço móvel")
    mobile_service_amount: Optional[float] = Field(None, description="Valor para o serviço móvel")
    fiber: Optional[Literal["Básico", "Intermediário", "Família"]] = Field(None, description="Plano de fibra")
    fiber_amount: Optional[float] = Field(None, description="Valor do plano de fibra")
    streaming_partnership: Optional[Literal["GloboPlay", "HBO Max"]] = Field(None, description="Parceria com streaming")
    fixed_phone: Optional[bool] = Field(None, description="Telefone fixo incluído no pacote")
    price: float = Field(..., gt=0, description="Preço total do pacote")
    is_b2b: bool = Field(..., description="Define se o pacote é para empresas (B2B)")

    @model_validator(mode="after")
    def validate_single_plan(cls, values):
        mobile_service = values.mobile_service
        fiber = values.fiber
        fixed_phone = values.fixed_phone

        # Valida que apenas um tipo de plano foi preenchido
        plans = [bool(mobile_service), bool(fiber), bool(fixed_phone)]
        if sum(plans) != 1:
            raise ValueError("Você deve preencher apenas um dos planos: Serviço Móvel, Fibra ou Telefone Fixo.")
        
        return values
