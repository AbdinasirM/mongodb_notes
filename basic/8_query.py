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

Filter the Result

When finding documents in a collection, you can filter the
result by using a query object.

The first argument of the find() method is a query object, 
and is used to limit the search.

'''

try :
    #create a movie DB
    movieDB = client["MoviesDB"]

    #create a collection
    collection2 = movieDB["collection2"]
#     collection2.insert_many([
#   {
#     "Title": "Avatar",
#     "Year": "2009",
#     "Rated": "PG-13",
#     "Released": "18 Dec 2009",
#     "Runtime": "162 min",
#     "Genre": "Action, Adventure, Fantasy",
#     "Director": "James Cameron",
#     "Writer": "James Cameron",
#     "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
#     "Plot": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
#     "Language": "English, Spanish",
#     "Country": "USA, UK",
#     "Awards": "Won 3 Oscars. Another 80 wins & 121 nominations.",
#     "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
#     "Metascore": "83",
#     "imdbRating": "7.9",
#     "imdbVotes": "890,617",
#     "imdbID": "tt0499549",
#     "Type": "movie",
#     "Response": "True",
#     "Images": [
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTYyMzUxNl5BMl5BanBnXkFtZTcwNTg0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM2MDk3MTcyMV5BMl5BanBnXkFtZTcwNjg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2ODQ3NjMyMl5BMl5BanBnXkFtZTcwODg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxOTEwNDcxN15BMl5BanBnXkFtZTcwOTg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg1Nzk1MV5BMl5BanBnXkFtZTcwMDk0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
#     ]
#   },
#   {
#     "Title": "I Am Legend",
#     "Year": "2007",
#     "Rated": "PG-13",
#     "Released": "14 Dec 2007",
#     "Runtime": "101 min",
#     "Genre": "Drama, Horror, Sci-Fi",
#     "Director": "Francis Lawrence",
#     "Writer": "Mark Protosevich (screenplay), Akiva Goldsman (screenplay), Richard Matheson (novel), John William Corrington, Joyce Hooper Corrington",
#     "Actors": "Will Smith, Alice Braga, Charlie Tahan, Salli Richardson-Whitfield",
#     "Plot": "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.",
#     "Language": "English",
#     "Country": "USA",
#     "Awards": "9 wins & 21 nominations.",
#     "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU4NzMyNDk1OV5BMl5BanBnXkFtZTcwOTEwMzU1MQ@@._V1_SX300.jpg",
#     "Metascore": "65",
#     "imdbRating": "7.2",
#     "imdbVotes": "533,874",
#     "imdbID": "tt0480249",
#     "Type": "movie",
#     "Response": "True",
#     "Images": [
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI0NTI4NjE3NV5BMl5BanBnXkFtZTYwMDA0Nzc4._V1_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIwMDg2MDU4M15BMl5BanBnXkFtZTYwMTA0Nzc4._V1_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MDM1OTU5OV5BMl5BanBnXkFtZTYwMjA0Nzc4._V1_.jpg",
#       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0MTI2NjMzMzFeQTJeQWpwZ15BbWU2MDMwNDc3OA@@._V1_.jpg"
#     ]
#   },
# ])

#get the movie(s) from 2009
   
    # myquery = {"Year":{"$gt": "2010"} }
    # for document in collection2.find(myquery, {"_id": 0, "Title": 1, "imdbRating": 1}):
    #     print(document)


    myquery = {
        "$and": [
            {"Year":{"$gt": "2010"}},
            {"imdbRating": {"$ne": "N/A"}}
        ]
    }

    # # Specify projection with only "Title" and "imdbRating"
    for document in collection2.find(myquery, {"_id": 0, "Title": 1, "imdbRating": 1}):
        print(document)

except Exception as e:
    print("An error has occurred:", e)