from fastapi import Response

class LogoutUseCase:
    def execute(self, response: Response):
        # Remove o cookie de autenticação
        response.delete_cookie("director_auth_token")
        return {"status": "success", "message": "Logout realizado com sucesso"}
