from mongoengine import *


class UserInfoData(Document):
    pseudo = StringField(required=True, unique=True)
    password = StringField(required=True)
    email = StringField(required=True)
    nom = StringField(required=True)
    prenom = StringField(required=True)
    birthday = DateTimeField(required=True)
    country = StringField(required=False)
    city = StringField(required=False)
    language = StringField(required=False, default="fr_FR")
    xp = IntField(required=True, default=0)
    musclor = IntField(required=True, default=0)
    profilPicture = StringField(required=False)

    meta = {'collection': 'users'}
