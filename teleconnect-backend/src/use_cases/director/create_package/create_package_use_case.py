from repositories.package_repository import PackageRepository
from use_cases.director.create_package.create_package_dto import CreatePackageDTO
from entities.package import Package
from fastapi import Request, Response

class CreatePackageUseCase:
    def __init__(self, package_repository: PackageRepository):
        self.package_repository = package_repository

    def execute(self, create_package_dto: CreatePackageDTO, response: Response, request: Request):
        # Validação
        if (
            not create_package_dto.mobile_service
            or not create_package_dto.fiber
            or not create_package_dto.streaming_partnership
            or create_package_dto.price is None
            or create_package_dto.is_b2b is None  # Novo campo obrigatório
        ):
            response.status_code = 400
            return {"status": "error", "message": "Faltam informações obrigatórias para criar o pacote."}

        if create_package_dto.mobile_service == "Pós-pago" and create_package_dto.mobile_service_amount is None:
            response.status_code = 400
            return {"status": "error", "message": "O valor para o serviço móvel Pós-pago é obrigatório."}

        if create_package_dto.fiber_amount is None:
            response.status_code = 400
            return {"status": "error", "message": "O valor do plano de fibra é obrigatório."}

        # Criação do pacote
        package = Package(
            _id="",
            mobile_service=create_package_dto.mobile_service,
            mobile_service_amount=create_package_dto.mobile_service_amount,
            fiber=create_package_dto.fiber,
            fiber_amount=create_package_dto.fiber_amount,
            streaming_partnership=create_package_dto.streaming_partnership,
            fixed_phone=create_package_dto.fixed_phone,
            price=create_package_dto.price,
            is_b2b=create_package_dto.is_b2b  # Novo campo
        )

        # Salva no repositório
        try:
            self.package_repository.save(package)
            response.status_code = 201
            return {"status": "success", "message": "Pacote criado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao salvar o pacote: {str(e)}"}
