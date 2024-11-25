from pymongo import MongoClient
import gridfs
from bson import ObjectId

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

db = client["myfiles"]


# Create a GridFS bucket
bucket = gridfs.GridFSBucket(db)

# To rename a file in GridFS, use the rename() method. This requires the file’s _id.

bucket.rename(ObjectId("673282886aaa679ee8df32b6"), "updatedname.txt")

This changes the file’s name to "new_file_name.txt".