from pymongo import MongoClient

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

result = db.photos.drop()
