import pymongo
if __name__ == "__main__":
    print("Hello this is mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    showAllDataBase = client.list_database_names()
    print(showAllDataBase)
    #It will show the all collection in the database
    collection = client['Subhash']
    print(collection.list_collection_names())