from fastapi import APIRouter
from use_cases.user.user_packages.my_packages import router as my_packages_router
from use_cases.user.user_packages.add_package import router as add_package_router

router = APIRouter()
router.include_router(my_packages_router, tags=["User Packages"])
router.include_router(add_package_router, tags=["User Packages"])
