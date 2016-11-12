from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.restaurants.find({"address.zipcode": "10075"})

for document in cursor:
    print(document)

print(cursor.count())
