import pymongo
if __name__ == "__main__":
    print("Hello this is mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Subhash']
    collection =  db['Test']
    # create a data
    dic = {'name' : 'Subhash', 'age' : 20}
    dic1 = {'name2' : 'Dippu', 'age' : 21}
    # Insert Single data
    collection.insert_one(dic)
    # here find will find the all data with name : Subhash
    # Here Name : 1 means only  the Name is going to show
    # Here '_id': 0 means id is not going to show
    # Here limit show the no: of name 
    # allDocs = collection.find({'Name': 'Subhash'}, {'Name': 1, '_id': 0}).limit(1)
    allDocs = collection.find({'Name': 'Omkar', "Marks": {"$lte": 80}}) # Here this will print all marks of Omkar below 80

    for item in allDocs:
        print(item)
    