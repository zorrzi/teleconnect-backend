from repositories.package_repository import PackageRepository
from fastapi import Response

class ListPackagesUseCase:
    def __init__(self, package_repository: PackageRepository):
        self.package_repository = package_repository

    def execute(self, response: Response):
        try:
            packages = self.package_repository.list_all_packages()
            response.status_code = 200
            return {"status": "success", "data": packages}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao listar pacotes: {str(e)}"}
