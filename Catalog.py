import requests
class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
        self.hat = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()["data"]]
        self.collectibles = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()["data"]]
        self.premium = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()["data"]]
        self.featured = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()["data"]]
        self.clothing = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()["data"]]
        self.hair = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()["data"]]
        self.face = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()["data"]]
        self.neck = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()["data"]]
        self.shoulder = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()["data"]]
        self.front = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()["data"]]
        self.back = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()["data"]]
        self.waist = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()["data"]]
    @property
    async def Hats(self):
        return self.hat
    @property
    async def Collectibles(self):
        return self.collectibles
    @property
    async def Premium(self):
        return self.premium
    @property
    async def Featured(self):
        return self.Featured
    @property
    async def Clothing(self):
        return self.clothing
    @property
    async def Hair(self):
        return self.hair
    @property
    async def Face(self):
        return self.face
    @property
    async def Neck(self):
        return self.neck
    @property
    async def Shoulder(self):
         return self.shoulder
    @property
    async def Front(self):
         return self.front
    @property
    async def Back(self):
         return self.back
    @property
    async def Waist(self):
         return self.waist











            






