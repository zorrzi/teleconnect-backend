from repositories.package_repository import PackageRepository
from use_cases.director.update_package.update_package_dto import UpdatePackageDTO
from fastapi import Request, Response

class UpdatePackageUseCase:
    def __init__(self, package_repository: PackageRepository):
        self.package_repository = package_repository

    def execute(self, package_id: str, update_package_dto: UpdatePackageDTO, response: Response, request: Request):
        # Verifica se o pacote existe
        package = self.package_repository.get_package_by_id(package_id)
        if not package:
            response.status_code = 404
            return {"status": "error", "message": "Pacote não encontrado."}

        # Atualiza os campos
        updated_fields = update_package_dto.dict(exclude_unset=True)
        try:
            self.package_repository.update_package(package_id, updated_fields)
            response.status_code = 200
            return {"status": "success", "message": "Pacote atualizado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao atualizar o pacote: {str(e)}"}
