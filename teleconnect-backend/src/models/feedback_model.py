from mongoengine import Document, StringField, IntField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class FeedbackModel(Document):
    user_name = StringField(required=True)
    message = StringField(required=True)
    stars = IntField(min_value=1, max_value=5, required=True)

    @staticmethod
    def get_normal_fields():
        """
        Retorna os campos normais (não sensíveis) do documento.
        """
        return [
            i
            for i in FeedbackModel.__dict__.keys()
            if i[:1] != "_" and i not in ["sensivity_fields"]
        ]
