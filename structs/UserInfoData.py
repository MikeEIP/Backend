from mongoengine import StringField, DateTimeField, Document, IntField, ListField


class UserInfoData(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    email = StringField(required=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    birthday = DateTimeField(required=True)
    country = StringField(required=False)
    city = StringField(required=False)
    language = StringField(required=False, default="fr_FR")
    xp = IntField(required=True, default=0)
    musclor = IntField(required=True, default=0)
    profilPicture = StringField(required=False)
    friends = ListField(StringField(required=False), required=False)
    friendsWaitingList = ListField(StringField(required=False), required=False)

    meta = {'collection': 'users'}
