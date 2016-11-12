from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://mongodb0.example.net:27017")
db = client.primer

coll = db.dataset
print(coll)
