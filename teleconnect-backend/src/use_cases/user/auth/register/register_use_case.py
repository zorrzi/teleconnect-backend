from repositories.user_repository import UserRepository
from use_cases.user.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.user import User

class RegisterUseCase:
    user_repository = UserRepository

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password or not register_dto.cpf or not register_dto.phone:
            response.status_code = 406
            return{"status": "error", "message": "Não foi possível fazer cadastro, preencha todos os campos"}

        user = User(**register_dto.model_dump())

        self.user_repository.save(user)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do diretor com sucesso"}