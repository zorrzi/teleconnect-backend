from repositories.package_repository import PackageRepository
from fastapi import Response

class DeletePackageUseCase:
    def __init__(self, package_repository: PackageRepository):
        self.package_repository = package_repository

    def execute(self, package_id: str, response: Response):
        try:
            package = self.package_repository.get_package_by_id(package_id)
            if not package:
                response.status_code = 404
                return {"status": "error", "message": "Pacote não encontrado."}

            self.package_repository.delete_package(package_id)
            response.status_code = 200
            return {"status": "success", "message": "Pacote deletado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao deletar o pacote: {str(e)}"}
