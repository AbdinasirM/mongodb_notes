'''
Sort the Result

Use the sort() method to sort the result in ascending 
or descending order.

The sort() method takes one parameter for "fieldname" 
and one parameter for "direction" 
(ascending is the default direction).

'''

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


try:
     #create a movie DB
    movieDB = client["MoviesDB"]

    #create a collection
    collection2 = movieDB["collection2"]

    document = collection2.find({}, {"_id":0, "Title":1, "Year":1, "imdbVotes":1}).sort("Title")

    for doc in document:
        print(doc)

except Exception as e:
    print("Error has occured ", e)