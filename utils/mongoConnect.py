import datetime
import mongoengine.connection
from mongoengine import *
from mongoengine.connection import *
from mongoengine.connection import (MongoEngineConnectionError, get_db,
                                    get_connection)
from pip._vendor.requests.packages.urllib3.util import timeout

from utils.getConfig import Config
import app_var
import sys


def connectToMongo():
    mongoConfig = Config(app_var.CONFIG_PATH)

    url = mongoConfig.getField("mongo", "url")
    port = int(mongoConfig.getField("mongo", "port"))
    username = mongoConfig.getField("mongo", "username")
    password = mongoConfig.getField("mongo", "password")
    db = mongoConfig.getField("mongo", "db")

    print("\n===== MONGO =====")
    print("\tConnecting to mongo: " + url + ":" + str(port) + "\n\tuser/pass: " + username + " " + password + "\n\tdb: " + db)
    connect(db=db, host=url, port=port, username=username, password=password)
    conn = mongoengine.connection.get_connection() # type: mongoengine.connection.MongoClient
    try:
        print("\tConnecting to db... (if it take more than 20sec, you can stop the script, connection failed")
        conn.get_database("mike")
    except Exception as e:
        print("ERROR: Can't connect to DB or DB name invalid. Full error is:\n" + str(e))
        sys.exit(1)


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
"""
