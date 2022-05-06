import requests
class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
        self.hat = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()["data"]]
        print(self.hat)
        self.collectibles = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()["data"]]
        self.premium = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()["data"]]
        self.featured = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()["data"]]
        self.clothing = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()["data"]]
        self.hair = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()["data"]]
        self.face = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()["data"]]
        self.neck = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()["data"]]
        self.shoulder = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()["data"]]
        self.front = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()["data"]]
        self.back = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()["data"]]
        self.waist = [x for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()["data"]]
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



