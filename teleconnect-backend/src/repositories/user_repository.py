from models.user import User as UserModel
from entities.user import User
from utils.security import hash_password

def create_user(user_data: User):
    hashed_password = hash_password(user_data.password)
    user = UserModel(
        cpf=user_data.cpf,
        phone=user_data.phone,
        email=user_data.email,
        password=hashed_password,
        name=user_data.name
    )
    user.save()
    return user_data

def get_user_by_email(email: str):
    return UserModel.objects(email=email).first()
