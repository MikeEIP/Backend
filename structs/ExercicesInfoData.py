from mongoengine import *


class ExercicesInfoData(Document):
    exercise = StringField(required=True)
    difficulty = IntField(required=True)
    finished = StringField(required=True)
    time = DateTimeField(required=True)
    date = DateTimeField(required=True)
#    id= IntField(required=True)

    meta = {'collection': 'exercices'}

class Trainings(Document):
    exercices = ListField(ReferenceField(ExercicesInfoData))

    meta = {'collection': 'trainings'}