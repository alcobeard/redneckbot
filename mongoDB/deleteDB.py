from pymongo import MongoClient
#include pprint for readabillity of the
from pprint import pprint

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

result = db.drivers.delete_many({'name': 'Maksim'})

print('The number of name Maksim after delete:')
Maksim = db.drivers.find({'name': 'Maksim'}).count()
print(Maksim)

db.drivers.drop()
