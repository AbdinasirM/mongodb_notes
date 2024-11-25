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


'''
To download a file from GridFS, use either open_download_stream_by_name() (by filename) or open_download_stream() (by file _id).
'''

# this is great for text/json files

#Download by Filename: This retrieves the latest version of the file with the specified filename.

#ask = input("what file do you want to install")

# with bucket.open_download_stream_by_name("proxmox-ve_8.2-2.iso") as grid_out:
#     file_data = grid_out.read()
#     print("Downloaded content:", file_data)


#Download by File ID: Use this method when you have the specific _id of the file.

file_id = ObjectId("673282886aaa679ee8df32b6")  # Replace with actual file ID

with bucket.open_download_stream(file_id) as grid_out:
    file_data = grid_out.read()
    print("Downloaded content:", file_data)



'''
In both cases, file_data contains the file’s content as binary data.

'''
