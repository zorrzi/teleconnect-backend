from fastapi import APIRouter, Response, Request, Depends
from use_cases.director.create_package.create_package_dto import CreatePackageDTO
from use_cases.director.create_package.create_package_use_case import CreatePackageUseCase
from repositories.package_repository import PackageRepository
from middlewares.validate_director_auth_token import validade_director_auth_token

router = APIRouter()

# Inicializa o repositório e o caso de uso
create_package_use_case = CreatePackageUseCase(PackageRepository())

@router.post("/admin/create-package")
def create_package(create_package_dto: CreatePackageDTO, response: Response, request: Request):
    return create_package_use_case.execute(create_package_dto, response, request)


