from flask import Flask, request
import json
from Catalog import Catalog
import asyncio
app = Flask(__name__)
Catalog = Catalog()
async def Get_data(chosen):
    x = [("Hats", Catalog.Hats), ("Premium", Catalog.Premium), ("Collectibles", Catalog.Collectibles), ("Clothing", Catalog.Clothing), ("Hair", Catalog.Hair), ("Face", Catalog.Face), ("Neck", Catalog.Neck), ("Shoulder", Catalog.Shoulder), ("Front", Catalog.Front), ("Back", Catalog.Back), ("Waist", Catalog.Waist)]
    for z in x:
        if chosen == x[0]:
            await x[1]
        else:
            continue
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
