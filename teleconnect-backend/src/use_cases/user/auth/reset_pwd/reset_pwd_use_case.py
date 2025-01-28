from repositories.director_repository import DirectorsRepository
from fastapi import Request, Response
from use_cases.director.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from datetime import datetime

class ResetPwdUseCase:
    director_repository: DirectorsRepository

    def __init__(self, director_repository: DirectorsRepository):
        self.director_repository = director_repository

    def execute(self, reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
        check_exists = self.director_repository.find_by_reset_pwd_token(token=reset_pwd_dto.token)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar o diretor com o token fornecido"}

        doctor = check_exists[0]

        if doctor.reset_pwd_token_sent_at - datetime.now().timestamp() > 900:
            response.status_code = 400
            return {"status": "error", "message": "O token de redefinição expirou. Por favor, solicite um novo."} 
        
        self.director_repository.update_pwd(doctor.id, reset_pwd_dto.password)

        self.director_repository.update_reset_pwd_token(email=doctor.email, sent_at=0, token="")
        
        return {"status": "success", "message": "Senha alterada com sucesso, faça login para poder entrar em sua conta."}