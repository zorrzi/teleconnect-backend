from fastapi import APIRouter, Response
from use_cases.director.auth.logout.logout_use_case import LogoutUseCase

router = APIRouter()
logout_use_case = LogoutUseCase()

@router.post("/director/auth/logout")
def logout(response: Response):
    return logout_use_case.execute(response)
