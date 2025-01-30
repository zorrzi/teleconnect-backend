from repositories.user_repository import UserRepository
from repositories.package_repository import PackageRepository
from fastapi import Response

class BuyPackageUseCase:
    def __init__(self, user_repository: UserRepository, package_repository: PackageRepository):
        self.user_repository = user_repository
        self.package_repository = package_repository

    def execute(self, user_id: str, package_id: str, response: Response):
        try:
            # Verifica se o usuário existe
            user = self.user_repository.find_by_id(user_id)
            if not user:
                response.status_code = 404
                return {"status": "error", "message": "Usuário não encontrado."}

            # Verifica se o pacote existe
            package = self.package_repository.get_package_by_id(package_id)
            if not package:
                response.status_code = 404
                return {"status": "error", "message": "Pacote não encontrado."}

            # Verifica se o pacote já está na lista do usuário
            if package_id in user.packages:
                response.status_code = 400
                return {"status": "error", "message": "Pacote já está na lista do usuário."}

            # Atualiza a lista de pacotes do usuário usando update
            self.user_repository.add_package_to_user(user_id, package_id)

            response.status_code = 200
            return {"status": "success", "message": "Pacote adicionado com sucesso."}

        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao adicionar pacote: {str(e)}"}
