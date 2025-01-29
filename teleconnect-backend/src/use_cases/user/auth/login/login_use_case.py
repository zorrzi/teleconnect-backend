from repositories.user_repository import UserRepository
from fastapi import FastAPI, Request, Response
from use_cases.user.auth.login.login_dto import LoginDTO
from entities.user import User
import jwt
import os

class LoginUseCase:
    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.user_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Erro ao fazer Login"}

        user = check_exists[0]

        if (not user.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        token = jwt.encode({"email": user.email, "id": str(user.id)}, os.getenv("USER_JWT_SECRET"))
        print(f"Token gerado: {token}")


        response.set_cookie(
        key="user_auth_token",
        value=f"Bearer {token}",
        httponly=True,
        path="/",
        secure=False,  # Altere para True em produção com HTTPS
        samesite="Lax"  # Altere para 'Strict' se necessário
    )
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}