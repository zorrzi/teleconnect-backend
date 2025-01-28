from fastapi import APIRouter, Response, Request
from use_cases.director.update_package.update_package_dto import UpdatePackageDTO
from use_cases.director.update_package.update_package_use_case import UpdatePackageUseCase
from repositories.package_repository import PackageRepository

router = APIRouter()

# Inicializa o repositório e o caso de uso
update_package_use_case = UpdatePackageUseCase(PackageRepository())

@router.put("/admin/update-package/{package_id}")
def update_package(package_id: str, update_package_dto: UpdatePackageDTO, response: Response, request: Request):
    return update_package_use_case.execute(package_id, update_package_dto, response, request)
