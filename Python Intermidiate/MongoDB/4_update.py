import pymongo
if __name__ == "__main__":
    print("Hello this is mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Subhash']
    collection =  db['Test']
    prev = {"Name": "Subhash"}
    nextt = {"$set": {"Location": "Mumbai"}}
    # collection. update_one(prev, nextt) # Here this will update one data
    cont = collection. update_many (prev, nextt) # Here this will update all data
    print(cont.modified_count) # Here this will count all updated data