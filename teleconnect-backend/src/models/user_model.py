from mongoengine import Document, EmailField, StringField, IntField, ReferenceField
from models.package_model import PackageModel
import datetime
from mongoengine.fields import EmailField, StringField, IntField, ListField
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class UserModel(Document):
    sensivity_fields = [
        
    ]
    cpf = StringField(required=True, unique=True)
    phone = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True)
    packages = ListField(StringField(), default=[])

    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    def get_normal_fields():
        return [i for i in UserModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in UserModel.sensivity_fields]
    
    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()

    def check_password_matches(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))