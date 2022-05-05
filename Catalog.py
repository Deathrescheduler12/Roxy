import requests
class Catalog:
    def __init__(self):
        self.hat = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=HeadAccessories").json()["data"]]
        self.collectibles = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit=120&subcategory=Collectibles").json()["data"]]
        self.premium = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit=120&subcategory=Premium").json()["data"]]
        self.featured = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit=120&subcategory=Featured").json()["data"]]
        self.clothing = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit=120&subcategory=Clothing").json()["data"]]
        self.hair = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=HairAccessories").json()["data"]]
        self.face = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=FaceAccessories").json()["data"]]
        self.neck = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=NeckAccessories").json()["data"]]
        self.shoulder = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=ShoulderAccessories").json()["data"]]
        self.front = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=FrontAccessories").json()["data"]]
        self.back = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=BackAccessories").json()["data"]]
        self.waist = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit=120&subcategory=WaistAccessories").json()["data"]]
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











            






