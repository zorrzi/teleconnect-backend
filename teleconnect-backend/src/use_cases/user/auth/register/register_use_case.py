from repositories.user_repository import UserRepository
from use_cases.user.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.user import User

class RegisterUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        # Valida se todos os campos obrigatórios estão preenchidos
        if not all([register_dto.name, register_dto.email, register_dto.password, register_dto.cpf, register_dto.phone]):
            response.status_code = 400
            return {"status": "error", "message": "Todos os campos são obrigatórios."}

        # Verifica se já existe um usuário com o mesmo email ou CPF
        existing_user = self.user_repository.find_by_email(register_dto.email)
        if existing_user:
            response.status_code = 409
            return {"status": "error", "message": "Já existe um usuário com este email."}

        # Criação do novo usuário
        try:
            user = User(
                cpf=register_dto.cpf,
                phone=register_dto.phone,
                email=register_dto.email,
                password=register_dto.password,
                name=register_dto.name,
                packages=register_dto.packages  # Lista de pacotes inicial (pode ser vazia)
            )
            self.user_repository.save(user)

            response.status_code = 201
            return {"status": "success", "message": "Usuário registrado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao registrar usuário: {str(e)}"}
