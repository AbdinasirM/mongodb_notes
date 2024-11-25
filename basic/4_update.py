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
Update Collection

You can update a record, or document as it is called in MongoDB, by using the update_one() method.

The first parameter of the update_one() method is a query object defining which document to update.

'''


try:
    #create a movie DB
    movieDB = client["MoviesDB"]

    #create a collection
    collection2 = movieDB["collection2"] 

    myquery = {
        "$and": [
            {"Year":{"$gt": "2010"}},
            {"imdbRating": {"$eq": "N/A"}}
        ]
    }

    imdbRating = {"$set": {"imdbRating":"5"}}
    collection2.update_one(myquery, imdbRating)

except Exception as e:
    print("Error has occured", e)