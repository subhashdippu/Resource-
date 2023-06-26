import pymongo
if __name__ == "__main__":
    print("Hello this is mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Subhash'] # Current database and create a database
    collection =  db['Test']
    # create a data
    dic = {'name' : 'Subhash', 'age' : 20}
    dic1 = {'name2' : 'Dippu', 'age' : 21}
    # Insert Single data
    collection.insert_one(dic)
    # Insert many data 
    # you can custumize the uniqe id by '_id' : 4,
    Insert = [
        {'_id': 1, 'Name' : 'Subhash', 'Location' : 'Delhi', 'Marks' : 100},
        {'_id': 2,'Name' : 'Dippu', 'Location' : 'Bihar', 'Marks' : 99},
        {'_id': 3,'Name' : 'Shiv', 'Location' : 'Mumbai', 'Marks' : 95},
        {'_id': 4,'Name' : 'Omkar', 'Location' : 'Dehradun', 'Marks' : 58},
        {'_id': 5,'Name' : 'Sank', 'Location' : 'Delhi', 'Marks' : 87},
    ]
    collection.insert_many(Insert)
    