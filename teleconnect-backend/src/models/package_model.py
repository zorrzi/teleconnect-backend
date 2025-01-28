from mongoengine import Document, StringField, FloatField, BooleanField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PackageModel(Document):
    mobile_service = StringField(choices=["Pré-pago", "Pós-pago"], required=True)
    mobile_service_amount = FloatField()
    fiber = StringField(choices=["Básico", "Intermediário", "Família"], required=True)
    fiber_amount = FloatField()
    streaming_partnership = StringField(choices=["GloboPlay", "Premiere"], required=True)
    fixed_phone = BooleanField(required=True)
    price = FloatField(required=True)
    is_b2b = BooleanField(required=True)

    @staticmethod
    def get_normal_fields():
        return [
            i
            for i in PackageModel.__dict__.keys()
            if i[:1] != "_" and i not in ["sensivity_fields"]
        ]
