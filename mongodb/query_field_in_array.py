from pymongo import MongoClient

client = MongoClient()
db = client.test
cursor = db.restaurants.find({"grades.grade": "B"})

# for document in cursor:
    # print(document)

print(cursor.count())
