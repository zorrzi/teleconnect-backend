import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.user import User
from models.user_model import UserModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class UserRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, user: User) -> None:
        user_model = UserModel()
        user_dict = user.model_dump()

        for k in UserModel.get_normal_fields():
            if (k not in user_dict):
                continue

            user_model[k] = user_dict[k]

        for k in UserModel.sensivity_fields:
            user_model[k] = SensivityField(fernet=self.fernet, data=user_dict[k])

        user_model.password = bcrypt.hashpw(f'{user.password}'.encode(), bcrypt.gensalt()).decode()

        user_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[UserModel]:
        result = UserModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[UserModel]:
        result = UserModel.objects(id=id).first()
        return result
    
    def get_all_users(self):
        """
        Retorna todos os usuários da base de dados.

        Returns:
            List[UserModel]: Lista de usuários.
        """
        try:
            users = UserModel.objects.all()
            return users
        except Exception as e:
            print(f"Erro ao buscar usuários: {str(e)}")
            return []
    
    def add_package_to_user(self, user_id: str, package_id: str) -> bool:
        user = self.find_by_id(user_id)
        if user:
            # Verifica se já está na lista
            if package_id not in user.packages:
                UserModel.objects(id=user_id).update_one(push__packages=package_id)
                return True
        return False


    def get_user_packages(self, user_id: str) -> List[str]:
        user = self.find_by_id(user_id)
        return user.packages if user else []
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        UserModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[UserModel]:
        result: list[UserModel] = UserModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        UserModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.name

    def get_email(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.email
    
    def update_name(self, id: str, name: str) -> None:
        UserModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        UserModel.objects(id=id).update(set__email = email)
        return None
    