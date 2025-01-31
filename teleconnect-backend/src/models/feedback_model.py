from mongoengine import Document, StringField, IntField, ReferenceField
import os
import dotenv
from cryptography.fernet import Fernet
from models.user_model import UserModel

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class FeedbackModel(Document):
    user_id = ReferenceField(UserModel, required=True)
    feedback_text = StringField(required=True, max_length=500)
    stars = IntField(required=True, min_value=0, max_value=5)

    
