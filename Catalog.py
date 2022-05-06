import requests
class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
        self.hat = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()
        print(self.hat)
        self.collectibles = requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()
        self.premium = requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()
        self.featured = requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()
        self.clothing = requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()
        self.hair = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()
        self.face = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()
        self.neck = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()
        self.shoulder = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()
        self.front = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()
        self.back = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()
        self.waist = requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()
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











            






