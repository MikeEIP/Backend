import datetime

from mongoengine import connect

import structs.UserInfoData

from utils.getConfig import Config

mongoConfig = Config("config.json")

url = mongoConfig.getField("mongo", "url")
port = int(mongoConfig.getField("mongo", "port"))

print("Connecting to mongo: " + url + ":" + str(port))

connect('mike', host=url, port=port)

# #Test
#
# dimitri = structs.UserInfoData.UserInfoData()
# dimitri.pseudo = "dimitri"
# dimitri.nom = "Wyzlic"
# dimitri.prenom = "Dimitri"
# dimitri.email = "dimitriwyzlic@gmail.com"
# dimitri.birthday = datetime.datetime.now()
#
# dimitri.save()
