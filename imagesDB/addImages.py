from pymongo import MongoClient
from pprint import pprint
from random import randint
import base64
import os

client = MongoClient("mongodb+srv://alcobeard:passw0rd@cluster0-vpyhn.mongodb.net/mongoDB?retryWrites=true&w=majority")
db = client.USA_Parts_SHOP

path = '../data/'
images = []

for filename in os.listdir(path):
    with open(path+filename, 'rb') as imageFile:
        img = base64.b64encode(imageFile.read())
    images.append(img)

for x in range(1, 651):
    img = images[randint(0, (len(images)-1))]
    len_img = len(img)

    images_db = {
        'image' : img
    }
    result=db.photos.insert_one(images_db)

    #Step 3: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1} with len {2}'.format(x,result.inserted_id,len_img))
#Step 4: Tell us that you are done
print('finished creating 500 images')
