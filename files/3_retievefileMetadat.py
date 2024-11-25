from pymongo import MongoClient
import gridfs


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

def calculateFileSize(length):
    if length < 1024:
        return f"{length} B"
    elif length < 1024**2:
        return f"{length / 1024:.2f} KB"
    elif length < 1024**3:
        return f"{length / 1024**2:.2f} MB"
    else:
        return f"{length / 1024**3:.2f} GB"



# Retrieve and display file metadata
for file in bucket.find({}):  # {} retrieves all files
    print("File ID:", file._id)
    print("Filename:", file.filename)
    print("Size:", calculateFileSize(file.length))
    print("Upload Date:", file.upload_date.strftime("%m/%d/%Y %I:%M:%S %p"))
    print("Metadata:", file.metadata)
    print("--------------------------------")