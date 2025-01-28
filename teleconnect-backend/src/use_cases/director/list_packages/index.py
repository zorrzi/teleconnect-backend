from fastapi import APIRouter, Response
from use_cases.director.list_packages.list_packages_use_case import ListPackagesUseCase
from repositories.package_repository import PackageRepository

router = APIRouter()

# Inicializa o repositório e o caso de uso
list_packages_use_case = ListPackagesUseCase(PackageRepository())

@router.get("/admin/list-packages")
def list_packages(response: Response):
    return list_packages_use_case.execute(response)
