from pymongo import MongoClient
url = "mongodb+srv://Bekkah93:Severus1993.@cluster0.vygwbkg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient (url)
db = client.pytech
print(db.list_collection_names)
