from mongoengine import Document, StringField, IntField, ReferenceField
from models.user_model import UserModel

class FeedbackModel(Document):
    user_id = ReferenceField(UserModel, required=True)  # Relacionado a um usuário
    feedback_text = StringField(required=True, max_length=500)  # Texto do feedback
    stars = IntField(required=True, min_value=1, max_value=5)  # Nota de 1 a 5
