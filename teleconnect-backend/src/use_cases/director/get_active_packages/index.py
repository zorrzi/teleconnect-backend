from fastapi import APIRouter, HTTPException
from repositories.user_repository import UserRepository
from repositories.package_repository import PackageRepository

router = APIRouter()
user_repository = UserRepository()
package_repository = PackageRepository()

@router.get("/admin/active-packages")
def get_active_packages():
    try:
        # Obtém todos os usuários
        users = user_repository.get_all_users()

        # Lista para armazenar todos os pacotes ativos
        active_packages = []

        for user in users:
            for package_id in user.packages:  # Assumindo que `user.packages` é uma lista de IDs de pacotes
                package = package_repository.find_by_id(package_id)
                if package:  # Se o pacote existe
                    active_packages.append({
                        "id": str(package.id),
                        "fiber": package.fiber,
                        "fiber_amount": package.fiber_amount,
                        "mobile_service": package.mobile_service,
                        "mobile_service_amount": package.mobile_service_amount,
                        "fixed_phone": package.fixed_phone,
                        "streaming_partnership": package.streaming_partnership,
                        "is_b2b": package.is_b2b,
                    })

        return {"status": "success", "data": active_packages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar pacotes ativos: {str(e)}")
