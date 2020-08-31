from pymongo import MongoClient
from pprint import pprint
import base64
from bson import objectid

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

ASingleDriver = db.drivers.find_one({})
print('A sample document:')
pprint(ASingleDriver)

with open('../data/dodge challenger.jpeg', 'rb') as imageFile:
    image1 = base64.b64encode(imageFile.read())
    print(image1)

with open('../data/jeep compass.jpeg', 'rb') as imageFile:
    image2 = base64.b64encode(imageFile.read())
    print(image2)


db.drivers.update_one(
    {'_id' : ASingleDriver.get('_id'), 'car.type': 'jeep cherokee'},
    {"$set": {"car.$.image1": image1, "car.$.image2": image2}})

UpdatedDocument = db.drivers.find_one({'_id':ASingleDriver.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)
