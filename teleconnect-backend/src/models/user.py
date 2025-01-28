from mongoengine import Document, StringField

class User(Document):
    cpf = StringField(required=True, unique=True)
    phone = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True)
