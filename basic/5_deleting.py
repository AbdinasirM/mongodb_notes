from pymongo import MongoClient 

# Define MongoDB connection parameters
host = "192.168.1.19"
port = 27017
username = "abdi"
password = "@abdi5520"
auth_database = "admin"

client = MongoClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource= auth_database
)


'''
Delete Document

To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is a 
query object defining which document to delete.
'''

# try:

#     #create a movie DB
#     movieDB = client["MoviesDB"]

#     #create a collection
#     collection2 = movieDB["collection2"]


#     myquery = {"Title":"Avatar"}
#     collection2.delete_one(myquery) 



# except Exception as e:
#     print("Error has occured", e)



'''
Delete Many Documents

To delete more than one document, use the delete_many() method.

The first parameter of the delete_many() method is a query object defining which documents to delete.

'''


try:
    
    #create a movie DB
    movieDB = client["MoviesDB"]

    #create a collection
    collection2 = movieDB["collection2"]
    
    
    #Delete all documents were the address starts with the letter I:
    
    myquery = { "Title": {"$regex": "^I"} }
    
    x = collection2.delete_many(myquery)

    print(x.deleted_count, " documents deleted.") 



except Exception as e:
    print("Error has occured", e)
