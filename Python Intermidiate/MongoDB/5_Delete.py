import pymongo
if __name__ == "__main__":
    print("Hello this is mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Subhash']
    collection =  db['Test']
    rec = {"name": "Subhash"}
    # collection.delete_one(rec) # It will delete the first Subhash
    collection.delete_many(rec) # It will delete the all the Subhash