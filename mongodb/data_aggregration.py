from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.restaurants.aggregate(
    [
        {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
    ]
)
for document in cursor:
    print(document)
