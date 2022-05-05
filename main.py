from flask import Flask, request
import json
from Catalog import Catalog
import asyncio
app = Flask(__name__)
Catalog = Catalog()
async def Get_data(chosen):
    if chosen == "Premium":
        return await Catalog.Premium
    if chosen == "Collectibles":
        return await Catalog.Collectibles
    if chosen == "Featured":
        return await Catalog.Featured
    if chosen == "Clothing":
        return await Catalog.Clothing
    if chosen == "Hair":
        return await Catalog.Hair
    if chosen == "Face":
        return await Catalog.Face
    if chosen == "Neck":
        return await Catalog.Neck
    if chosen == "Shoulder":
        return await Catalog.Shoulder
    if chosen == "Front":
        return await Catalog.Front
    if chosen == "Back":
        return await Catalog.Back
    if chosen == "Waist":
        return await Catalog.Waist
@app.route("/get/items", methods=["GET"])
def get_catalog():
    for x, y in request.args.items():
        if x == "chosen":
            return json.dumps(asyncio.run(Get_data(y)))
        else:
            continue
#print(asyncio.run(Get_data()))
if __name__ == "__main__":
    app.run()
