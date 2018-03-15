from mongoengine import StringField, Document


class AdminInfoData(Document):
    username = StringField(required=True, unique=True, null=False)

    meta = {'collection': 'admin'}
