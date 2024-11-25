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
bucket = gridfs.GridFSBucket(db

'''
Uploading Dynamic Data: For cases where you want to upload data generated at runtime without saving it to a file, use open_upload_stream(). This creates an in-memory stream to which you can write data.
If you're using open_upload_stream with a with statement, it doesn’t return the file_id directly in the same way that upload_from_stream does. However, you can still access the file’s unique ID by using the grid_in._id attribute after the file stream is closed (i.e., outside the with block).

Here’s how you can retrieve and print the file_id after writing data with open_upload_stream:
'''

with bucket.open_upload_stream(
    'newfile2.txt', 
    chunk_size_bytes=1048576,
    metadata={"contentType": "text/plain"}
) as grid_in:
    grid_in.write("This is some examples test data".encode('utf-8'))

# Print the file ID after the upload stream is closed
print("File uploaded successfully with ID:", grid_in._id)

'''
Explanation

    grid_in._id: This attribute contains the unique ID of the file stored in GridFS. It is available after the with block (i.e., after the upload stream is closed).
    print(): The print() statement outputs the file ID, confirming the successful upload.
'''