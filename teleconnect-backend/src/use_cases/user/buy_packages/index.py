from pydantic import BaseModel
from fastapi import APIRouter, Response
from use_cases.user.buy_packages.buy_package_use_case import BuyPackageUseCase
from use_cases.user.buy_packages.buy_package_dto import BuyPackageDTO
from repositories.user_repository import UserRepository
from repositories.package_repository import PackageRepository



router = APIRouter()

user_repository = UserRepository()
package_repository = PackageRepository()
buy_package_use_case = BuyPackageUseCase(user_repository, package_repository)

@router.post("/user/buy-package")
def buy_package(request: BuyPackageDTO, response: Response):
    return buy_package_use_case.execute(request.user_id, request.package_id, response)
