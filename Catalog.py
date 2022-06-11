import requests
from database import database
import datetime

class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
        self.db = database(mongotoken)
    @property
    async def Hats(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Hats" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Hats" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Hats" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Hats" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Collectibles(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Collectibles" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Collectibles" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Collectibles" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Collectibles" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Premium(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Premium" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Premium" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Premium" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Premium" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Featured(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Featured" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Featured" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Featured" + str(datetime.datetime.day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()["data"]])
            data = self.db.get(str(datetime.datetime.month), _id = "Featured" + str(datetime.datetime.day))
            return data["items"]
    @property
    async def Clothing(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Clothing" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Clothing" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Clothing" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Clothing" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Hair(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Hair" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Hair" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Hair"+ str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Hair" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Face(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Face" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Face" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Face" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Face" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Neck(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Neck" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Neck" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Neck" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Neck" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Shoulder(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Shoulder" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Shoulder" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Shoulder" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Shoulder" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Front(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Front" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Front" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Front" + str(datetime.datetime.now().day),items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Front" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Back(self):
        if self.db.get(str(datetime.datetime.now().month), _id =  "Back" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id =  "Back" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Back" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Back" + str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Waist(self):
        if self.db.get(str(datetime.datetime.now().month), _id = "Waist" + str(datetime.datetime.now().day)):
            data = self.db.get(str(datetime.datetime.now().month), _id = "Waist" + str(datetime.datetime.now().day))
            return data["items"]
        else:
            self.db.add(_id = "Waist" + str(datetime.datetime.now().day), items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = "Waist" + str(datetime.datetime.now().day))
            return data["items"]
