# use_cases/user/packages/add_package.py

import os
import jwt
from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel
from repositories.user_repository import UserRepository
from repositories.package_repository import PackageRepository
from models.user_model import UserModel
from mongoengine.errors import DoesNotExist

router = APIRouter()
user_repository = UserRepository()
package_repository = PackageRepository()

class AddPackageRequest(BaseModel):
    packageId: str

@router.post("/user/add-package")
def add_package(
    data: AddPackageRequest,
    request: Request,
    response: Response,
):
    """
    Adiciona um pacote ao usuário logado. Lê o token no cookie `user_auth_token` manualmente.
    """
    # 1. Obtém o token do cookie
    token_cookie = request.cookies.get("user_auth_token")
    if not token_cookie:
        response.status_code = 401
        return {"status": "error", "message": "Token ausente ou usuário não autenticado"}

    try:
        # "Bearer <token>"
        token_str = token_cookie.replace("Bearer ", "")
        payload = jwt.decode(token_str, os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id") or payload.get("sub")  # dependendo de como foi gerado
    except (jwt.DecodeError, IndexError, AttributeError):
        response.status_code = 401
        return {"status": "error", "message": "Token inválido ou corrompido"}

    if not user_id:
        response.status_code = 401
        return {"status": "error", "message": "ID do usuário não encontrado no token"}

    # 2. Verifica se o user existe
    user = user_repository.find_by_id(user_id)
    if not user:
        response.status_code = 404
        return {"status": "error", "message": "Usuário não encontrado"}

    # 3. Verifica se o pacote existe
    package = package_repository.find_by_id(data.packageId)
    if not package:
        response.status_code = 404
        return {"status": "error", "message": "Pacote não encontrado"}

    # 4. Tenta adicionar o pacote
    success = user_repository.add_package_to_user(user_id, data.packageId)
    if not success:
        response.status_code = 400
        return {"status": "error", "message": "Pacote já existe na conta do usuário"}

    response.status_code = 200
    return {"status": "success", "message": "Pacote adicionado com sucesso"}
