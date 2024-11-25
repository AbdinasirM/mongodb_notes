from pymongo import MongoClient 

# Define MongoDB connection parameters
host = "192.168.1.42"
port = 27017
username = "abdi"
password = "abdi9006"
auth_database = "admin"

client = MongoClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource= auth_database
)

# Creating DB
try:

    #create a db
    montuDB = client["montudb"]

    # create a collection
    testcollection = montuDB["mycollection"]

    # add content to the collect
    content = testcollection.insert_one({"name":"abdi"})

    #check if the db exists
    alldbs = client.list_database_names()
    if "montudb" in alldbs:
        print("db exists")
    else:
        print("db doesnt exist")
except Exception as e:
    print("An error has occurred:", e)


# Creating Collection

try :
    #create a db
    collectioncreationgDB = client["colDB"]

    #create collection
    mycollection = collectioncreationgDB["mycol"]

    #insert document
    mycollection.insert_one({"firstCOllection": [1,2,3,]})



    allDB = client.list_database_names()

    allCollections = collectioncreationgDB.list_collection_names()

    #check if "mycol" collection exists
    if "mycol" in allCollections:
        print("the collection exists")
    else:
        print("collection doesnt exist!")

except Exception as e:
    print("An error has occurred:", e)


'''
Insert Into Collection

To insert a record, or document as it is called in MongoDB, into a collection,
we use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing the name(s)
and value(s) of each field in the document you want to insert.
'''

try:
    #create db 
    inserdb = client["inserdb"]


    #create collection
    mycol = inserdb["mycol"]

    #data
    # user = {"username": "abdi", "age":23}



    #insert one document to the collection
    # x = mycol.insert_one(user)


    '''
    Return the _id Field
    The insert_one() method returns a InsertOneResult object, which has a property, 
    inserted_id, that holds the id of the inserted document.
    '''

    # print(f"{x.inserted_id} has been added to the {inserdb.name}")


    '''
    Insert Multiple Documents

    To insert multiple documents into a collection in MongoDB, 
    we use the insert_many() method. 
    
    The first parameter of the insert_many() method is a list
    containing dictionaries with the data you want to insert:
    '''

    mylist = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]
    
    
    imy = mycol.insert_many(mylist)

    print(imy.inserted_ids)


except Exception as e:
    print("An error has occurred:", e)