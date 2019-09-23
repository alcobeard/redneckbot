from pymongo import MongoClient
#include pprint for readabillity of the
from pprint import pprint

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

# print(type(BarFood))
# for i in BarFood:
#     print(i)
# print('len of barfood')
# print(len(BarFood))
#
# print('Find by License Plate only one:')
# BarFood = db.drivers.find_one({'car.licence_plate': 6})
# print(type(BarFood) is dict)

# result = db.drivers.delete_many({'cuisine': 'Bar Food'})
#
# print('The number of cuisine Bar Food after delete:')
# BarFood = db.drivers.find({'cuisine': 'Bar Food'}).count()
# print(BarFood)

db.drivers.drop()