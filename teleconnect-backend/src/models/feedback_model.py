from mongoengine import Document, StringField, IntField, ReferenceField
from models.user_model import UserModel

class FeedbackModel(Document):
    user_id = ReferenceField(UserModel, required=True)
    feedback_text = StringField(required=True, max_length=500)
    stars = IntField(required=True, min_value=1, max_value=5)
