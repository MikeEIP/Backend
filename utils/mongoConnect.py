import datetime
from mongoengine import connect
from utils.getConfig import Config

mongoConfig = Config("config.json")

url = mongoConfig.getField("mongo", "url")
port = int(mongoConfig.getField("mongo", "port"))

print("Connecting to mongo: " + url + ":" + str(port))

connect('mike', host=url, port=port)

"""
import structs.ExercicesInfoData

exo = structs.ExercicesInfoData.ExercicesInfoData()
exo.date = datetime.datetime.now()
exo.exercise = "pompe"
exo.difficulty = 4
exo.finished = "yes"
#exo.id = 1
exo.time = datetime.datetime.now()

exo.save()

trainings = structs.ExercicesInfoData.Trainings()
trainings.exercices.append(exo)
trainings.exercices.append(exo)
trainings.exercices.append(exo)

trainings.save()
"""

# # #Test
# import structs.UserInfoData
#
# dimitri = structs.UserInfoData.UserInfoData()
# dimitri.pseudo = "dimitri"
# dimitri.password = "pass"
# dimitri.nom = "Wyzlic"
# dimitri.prenom = "Dimitri"
# dimitri.email = "dimitriwyzlic@gmail.com"
# dimitri.birthday = datetime.datetime.now()
#
# dimitri.save()


