from mongoengine import StringField, DateTimeField, Document, IntField, ListField


class ObjectivesData(Document):
    name = StringField(required=True, unique=True)
    description = StringField(required=True)
    picture = StringField(required=True)
    requirements = StringField(required=True)

    meta = {'collection': 'users'}
