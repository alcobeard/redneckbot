from pymongo import MongoClient
from pprint import pprint
from random import randint
import base64, os

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

#Step 1: Create sample data
names = ['Ivan','Maksim','Denis', 'Aleksandr', 'Ilya','Veronika','Dmitriy', 'Petr','Grigoriy', 'Semen','Arseny','Zosya', 'Ksenya']
mopar_car = ['dodge challenger','dodge charger','jeep cherokee','jeep compass','pontiac gto']

path = '../data/'
images = []

for filename in os.listdir(path):
    with open(path+filename, 'rb') as imageFile:
        img = base64.b64encode(imageFile.read())
    images.append(img)

for x in range(1, 101):
    name = names[randint(0, (len(names)-1))]
    img1 = images[randint(0, (len(images)-1))]
    img2 = images[randint(0, (len(images)-1))]

    USA_Parts_SHOP = {
        'name' : name,
        'date_of birth' : randint(1961,1999),
        'phone': randint(89000000000,89999999999),
        'car' : [
            {
                'model' : mopar_car[randint(0, (len(mopar_car)-1))],
                'date_of_production' : randint(2001,2019),
                'licence_plate' : randint(0,100),
                'image1': img1,
                'image2': img2
            },
        ],
        'owner': name
    }

    len_dr = len(USA_Parts_SHOP)
    #Step 2: Insert USA_Parts_SHOP object directly into MongoDB via isnert_one
    result=db.drivers.insert_one(USA_Parts_SHOP)

    #Step 3: Print to the console the ObjectID of the new document
    print('Created {0} of 100 as {1} with object len {2}'.format(x,result.inserted_id, len_dr))
#Step 4: Tell us that you are done
print('finished creating 100 drivers')
