import datetime
from pymongo import MongoClient
class database:
    def __init__(self, token):
        self.client = MongoClient(token)
        self.db = self.client[str(datetime.datetime.now().year)]
    def add(self, **item):
        dbname = self.db[str(datetime.datetime.now().month)]
        return dbname.insert_one(item).inserted_id
    def remove(self,**item):
        dbname = self.db[str(datetime.datetime.now().month)]
        return dbname.delete_one(item)
    def get(self, month, **item):
        dbname = self.db[month]
        if item == {}:
            return dbname.find(item)
        return dbname.find_one(item)
    def update(self, previousitem, item):
        dbname = self.db[datetime.datetime.now().month]
        return dbname.update_one(previousitem, item)
