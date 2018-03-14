from mongoengine import *


class AdminInfoData(Document):
    name = StringField(required=True, unique=True, null=False)

    meta = {'collection': 'admin'}