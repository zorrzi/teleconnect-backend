from fastapi import Request, Response, Depends
from fastapi import APIRouter
from .check_session_validity_use_case import CheckSessionValidatyUseCase
from middlewares.validate_director_auth_token import validade_director_auth_token

router = APIRouter()
check_session_validity_use_case = CheckSessionValidatyUseCase()

@router.post("/director/auth/check/token", dependencies=[Depends(validade_director_auth_token)])
def check_session_validity(response: Response, request: Request):
    return check_session_validity_use_case.execute(response, request)