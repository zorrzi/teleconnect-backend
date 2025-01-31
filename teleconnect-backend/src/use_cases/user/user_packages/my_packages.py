# use_cases/user/packages/my_packages.py

import os
import jwt
from fastapi import APIRouter, HTTPException, Request, Response
from repositories.user_repository import UserRepository
from repositories.package_repository import PackageRepository
from models.user_model import UserModel
from pydantic import BaseModel
from mongoengine.errors import DoesNotExist

router = APIRouter()
user_repository = UserRepository()
package_repository = PackageRepository()

@router.get("/user/my-packages")
def get_user_packages(request: Request, response: Response):
    """
    Retorna a lista de pacotes do usuário logado, decodificando manualmente o token do cookie.
    """

    token_cookie = request.cookies.get("user_auth_token")
    if not token_cookie:
        response.status_code = 401
        return {"status": "error", "message": "Token ausente ou usuário não autenticado"}

    try:
        token_str = token_cookie.replace("Bearer ", "")
        payload = jwt.decode(token_str, os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id") or payload.get("sub")
    except (jwt.DecodeError, IndexError, AttributeError):
        response.status_code = 401
        return {"status": "error", "message": "Token inválido ou corrompido"}

    if not user_id:
        response.status_code = 401
        return {"status": "error", "message": "ID do usuário não encontrado no token"}

    # Busca o usuário
    user = user_repository.find_by_id(user_id)
    if not user:
        response.status_code = 404
        return {"status": "error", "message": "Usuário não encontrado"}

    # Exemplo: user.packages é uma lista de IDs de pacotes
    if not user.packages:
        return {"status": "success", "data": []}

    # Para cada ID, busca os detalhes no package_repository
    # Se quiser retornar só os IDs, pode simplificar
    packages_detail = []
    for pkg_id in user.packages:
        pkg = package_repository.find_by_id(pkg_id)
        if pkg:
            packages_detail.append({
                "id": str(pkg.id),
                "price": pkg.price,
                "fiber": pkg.fiber,
                "mobile_service": pkg.mobile_service,
                "fixed_phone": pkg.fixed_phone,
                "is_b2b": pkg.is_b2b,
                # ... e quaisquer outros campos
            })

    return {"status": "success", "data": packages_detail}
