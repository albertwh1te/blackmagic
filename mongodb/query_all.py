from pymongo import MongoClient

client = MongoClient()
db = client.test
cursor = db.restaurants.find()

for document in cursor:
    print(document)
print(cursor.count())
