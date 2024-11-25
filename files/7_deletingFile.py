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


# To delete a file, you’ll also need the file’s _id. Use the delete() method to remove both the file’s metadata and all associated chunks.

bucket.delete(ObjectId("6732847fd9fe96c348781aa7"))
print("File deleted successfully.")