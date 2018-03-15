from mongoengine import *


class AdminInfoData(Document):
    username = StringField(required=True, unique=True, null=False)

    meta = {'collection': 'admin'}

