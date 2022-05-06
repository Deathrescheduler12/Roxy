import requests
class Catalog:
    def __init__(self, limit: int=60):
        self.limit = str(limit)
    @property
    async def Hats(self):
        try:
            return self.hats 
        except:
            self.hats = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HeadAccessories").json()["data"]]
            return self.hats
    @property
    async def Collectibles(self):
        try:
            return self.collectibles 
        except:
            self.collectibles = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Collectibles&limit={self.limit}&subcategory=Collectibles").json()["data"]]
            return self.collectibles
    @property
    async def Premium(self):
        try:
            return self.premium 
        except:
            self.premium = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Premium&limit={self.limit}&subcategory=Premium").json()["data"]]
            return self.premium
    @property
    async def Featured(self):
        try:
            self.featured 
        except:
            self.featured = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Featured&limit={self.limit}&subcategory=Featured").json()["data"]]
            return self.featured
    @property
    async def Clothing(self):
        try:
            return self.clothing
        except:
            self.clothing = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit={self.limit}&subcategory=Clothing").json()["data"]]
            return self.clothing
    @property
    async def Hair(self):
        try:
            return self.hair
        except:
            self.hair = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=HairAccessories").json()["data"]]
    @property
    async def Face(self):
        try:
            return self.face
        except:
            self.face = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FaceAccessories").json()["data"]]
            return self.face
    @property
    async def Neck(self):
        try:
            return self.neck
        except:
            self.neck = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=NeckAccessories").json()["data"]]
            return self.neck
    @property
    async def Shoulder(self):
        try:
            return self.shoulder
        except:
            self.shoulder = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=ShoulderAccessories").json()["data"]]
            return self.shoulder
    @property
    async def Front(self):
        try:
            return self.front
        except:
            self.front = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=FrontAccessories").json()["data"]]
            return self.front
    @property
    async def Back(self):
        try:
            return self.back
        except:
            self.back = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=BackAccessories").json()["data"]]
            return self.back
    @property
    async def Waist(self):
        try:
            return self.waist
        except:
            self.waist = [x["id"] for x in requests.get(f"https://catalog.roblox.com/v1/search/items?category=CommunityCreations&limit={self.limit}&subcategory=WaistAccessories").json()["data"]]
            return self.waist










            






