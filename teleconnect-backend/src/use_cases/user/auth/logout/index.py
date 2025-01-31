from fastapi import APIRouter, Response
from use_cases.user.auth.logout.logout_use_case import LogoutUseCase

router = APIRouter()
logout_use_case = LogoutUseCase()

@router.post("/user/auth/logout")
def logout(response: Response):
    return logout_use_case.execute(response)
