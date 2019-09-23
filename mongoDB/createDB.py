from pymongo import MongoClient
from pprint import pprint
from random import randint

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

#Step 2: Create sample data
names = ['Ivan','Maxim','Denis', 'Aleksandr', 'Ilya','Veronika','Dmitriy', 'Petr','Grigoriy', 'Semen','Arseny','Zosya', 'Ksenya']
date_of_birth = '01.01.1961'
mopar_car = ['dodge challenger','dodge charger','jeep cherokee','jeep compass','pontiac gto']
car_image = []
license_plate = ''

for x in range(1, 101):
    USA_Parts_SHOP = {
        'name' : names[randint(0, (len(names)-1))],
        'date_of birth' : randint(1961,1999),
        'car' : [
            {
                'type' : mopar_car[randint(0, (len(mopar_car)-1))],
                'date_of_production' : randint(2001,2019),
                'licence_plate' : randint(0,100)
            },
        ]
        # 'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        # 'rating' : randint(1, 5),
        # 'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
    }

    #Step 3: Insert USA_Parts_SHOP object directly into MongoDB via isnert_one
    result=db.drivers.insert_one(USA_Parts_SHOP)

    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 100 drivers')





