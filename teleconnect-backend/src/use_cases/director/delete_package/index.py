from fastapi import APIRouter, Response
from use_cases.director.delete_package.delete_package_use_case import DeletePackageUseCase
from repositories.package_repository import PackageRepository

router = APIRouter()

# Inicializa o repositório e o caso de uso
delete_package_use_case = DeletePackageUseCase(PackageRepository())

@router.delete("/admin/delete-package/{package_id}")
def delete_package(package_id: str, response: Response):
    return delete_package_use_case.execute(package_id, response)
