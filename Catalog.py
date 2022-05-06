import requests
from database import database
import datetime

class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
        self.db = database("mongodb+srv://mohamed:deeq1012@cluster0.9i97o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    @property
    async def Hats(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Hats"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Hats")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Hats", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Collectibles(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Collectibles"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Collectibles")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Collectibles", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Premium(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Premium"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Premium")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Premium", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Featured(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Premium"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Premium")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.day), asset = "Premium", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()["data"]])
            data = self.db.get(str(datetime.datetime.month), _id = str(datetime.datetime.day))
            return data["items"]
    @property
    async def Clothing(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Clothing"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Clothing")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Clothing", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Hair(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Hair"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Hair")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Hair", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Face(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Face"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Face")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Face", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Neck(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Neck"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Neck")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Neck", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Shoulder(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Shoulder"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Shoulder")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Shoulder", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Front(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Front"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Front")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Front", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Back(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Back"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Back")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Back", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
    @property
    async def Waist(self):
        if self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Waist"):
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day), asset="Waist")
            return data["items"]
        else:
            self.db.add(_id = str(datetime.datetime.now().day), asset = "Waist", items = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()["data"]])
            data = self.db.get(str(datetime.datetime.now().month), _id = str(datetime.datetime.now().day))
            return data["items"]
