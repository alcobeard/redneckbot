from pymongo import MongoClient
from pprint import pprint
from random import randint

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

def addDriver(name, date_of_birth, phone, mopar_car, date_of_production, license_plate):
    driver = {
        'name': name,
        'date_of birth': date_of_birth,
        'phone' : phone,
        'car': [
            {
                'type': mopar_car,
                'date_of_production': date_of_production,
                'licence_plate': license_plate
            },
        ]
    }
    # Step 3: Insert USA_Parts_SHOP object directly into MongoDB via isnert_one
    db.drivers.insert_one(driver)
    # Step 4: Print to the console the ObjectID of the new document
    return ('driver added')

def findDriverLP(license_plate):
    result_count = db.drivers.find({'car.licence_plate': license_plate}).count()

    if result_count == 0:
        return ('no drivers')
    elif result_count == 1:
        return (db.drivers.find_one({'car.licence_plate': license_plate}))
    else:
        for i in db.drivers.find({'car.licence_plate': license_plate}):
            return (i)

def findDriverCar(car_type):
    result_count = db.drivers.find({'car.type': car_type}).count()

    if result_count == 0:
        return ('no cars')
    elif result_count == 1:
        return (db.drivers.find_one({'car.type': car_type}))
    else:
        for i in db.drivers.find({'car.type': car_type}):
            return (i)

def deleteDriver(name):
    db.drivers.delete_one({'name': name})