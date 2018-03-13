import json


class getConfig:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.data = ""
        try:
            self.data = json.load(open('config.json'))
        except Exception as e:
            print("Can't load or parse file " + filePath + "error:\n" + str(e))
            raise e

    def getField(self, field: str, *fields) -> str or None:
        try:
            tmp = self.data[field]
            for ff in fields:
                tmp = tmp[ff]
            return tmp
        except Exception as e:
            print("Cant get field " + field + " " + str(fields) + " error:\n" + str(e))
            return None
