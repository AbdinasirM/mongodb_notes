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
In MongoDB we use the find() and find_one() methods 
to find data in a collection.

Just like the SELECT statement is used to find data in a
table in a MySQL database.
'''

#Find One

# try:
#     #create a movie DB
#     movieDB = client["MoviesDB"]

#     #create a collection
#     collection1 = movieDB["collection1"]

# #     #insert movie document
# #     ins = collection1.insert_one({
# #     "Title": "I Am Legend",
# #     "Year": "2007",
# #     "Rated": "PG-13",
# #     "Released": "14 Dec 2007",
# #     "Runtime": "101 min",
# #     "Genre": "Drama, Horror, Sci-Fi",
# #     "Director": "Francis Lawrence",
# #     "Writer": "Mark Protosevich (screenplay), Akiva Goldsman (screenplay), Richard Matheson (novel), John William Corrington, Joyce Hooper Corrington",
# #     "Actors": "Will Smith, Alice Braga, Charlie Tahan, Salli Richardson-Whitfield",
# #     "Plot": "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.",
# #     "Language": "English",
# #     "Country": "USA",
# #     "Awards": "9 wins & 21 nominations.",
# #     "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU4NzMyNDk1OV5BMl5BanBnXkFtZTcwOTEwMzU1MQ@@._V1_SX300.jpg",
# #     "Metascore": "65",
# #     "imdbRating": "7.2",
# #     "imdbVotes": "533,874",
# #     "imdbID": "tt0480249",
# #     "Type": "movie",
# #     "Response": "True",
# #     "Images": [
# #       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI0NTI4NjE3NV5BMl5BanBnXkFtZTYwMDA0Nzc4._V1_.jpg",
# #       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIwMDg2MDU4M15BMl5BanBnXkFtZTYwMTA0Nzc4._V1_.jpg",
# #       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MDM1OTU5OV5BMl5BanBnXkFtZTYwMjA0Nzc4._V1_.jpg",
# #       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0MTI2NjMzMzFeQTJeQWpwZ15BbWU2MDMwNDc3OA@@._V1_.jpg"
# #     ]
# #   })
#     #print(ins.inserted_id)
    

#     findingOne = collection1.find_one()
#     print(findingOne)
    

    
# except Exception as e:
#     print("An error has occurred:", e)




#find All
'''
To select data from a table in MongoDB, we can also use
 the find() method.

The find() method returns all occurrences in the selection.

The first parameter of the find() method is a query object.
In this example we use an empty query object, which selects 
all documents in the collection.
'''

try:
    
    #create a movie DB
    movieDB = client["MoviesDB"]

    #create a collection
    collection1 = movieDB["collection1"]

    # No parameters in the find() method gives you the same result as SELECT * in MySQL.
    # for document in collection1.find():
    #     print(document)

    # Return Only Some Fields
    '''

    The second parameter of the find() method is an object 
    describing which fields to include in the result.
    This parameter is optional, and if omitted, all fields 
    will be included in the result.
    
    '''

    #example:
    #Return only the names and addresses, not the _ids:

    for document in collection1.find({}, {"_id":0, "Year":1, "Title":1, "Type":1}):
        print(document)

except Exception as e:
    print("An error has occurred:", e)