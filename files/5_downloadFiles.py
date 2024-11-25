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
Save Downloaded Data to Disk: To save the downloaded content to a file on disk, write the data to a new file:

'''

# with bucket.open_download_stream_by_name('file.txt') as grid_out:
#     with open("downloaded_file.txt", "wb") as file:
#         file.write(grid_out.read())
# print("File downloaded successfully as 'downloaded_file.txt'")

with bucket.open_download_stream_by_name('proxmox-ve_8.2-2.iso') as grid_out:
    with open("proxmoxve8.iso", "wb") as file:
        file.write(grid_out.read())
print("File downloaded successfully as 'proxmoxve8.iso'")


# If you want to download a file from GridFS, you can handle different file types (like images, videos, ISO files, etc.) by simply saving them with the correct file extension. GridFS stores all files as binary data, so it doesn’t matter if the file is a text file, image, video, or any other format—downloading works the same way.

# The only adjustment you need to make is to save the file with the appropriate extension when you write it to disk. For example, if the file stored in GridFS is an image (file.jpg), save it as downloaded_file.jpg on your filesystem.
# Example for Downloading Different File Types

# Here’s how you can download any file type from GridFS by specifying the correct filename extension during saving:

# Assuming `filename` is the original filename in GridFS, e.g., "file.jpg" or "video.mp4"
filename = "file.jpg"  # Change this to the actual filename in GridFS

# Download the file from GridFS using its name
with bucket.open_download_stream_by_name(filename) as grid_out:
    # Save the file locally with the same filename or any desired filename
    with open("downloaded_" + filename, "wb") as file:
        file.write(grid_out.read())

print(f"File downloaded successfully as 'downloaded_{filename}'")

# Explanation

#     Specify the Filename: Use the filename stored in GridFS, such as "file.jpg" or "video.mp4". This example assumes you know the filename in GridFS and will save it with the same name, prefixed by "downloaded_".

#     Correct Extension: By saving the file with the correct extension, your system and applications will recognize the file type (e.g., .jpg for images, .mp4 for videos, .iso for disk images).

#     Binary Mode ("wb"): Opening the file in write-binary mode ("wb") is crucial for all file types, as it ensures that all data, including binary data, is saved correctly.

# Example Scenarios

# Here’s how it would look for different file types:
# Downloading an Image (e.g., .jpg)

filename = "image.jpg"
with bucket.open_download_stream_by_name(filename) as grid_out:
    with open("downloaded_" + filename, "wb") as file:
        file.write(grid_out.read())
print(f"Image downloaded successfully as 'downloaded_{filename}'")

# Downloading a Video (e.g., .mp4)

filename = "video.mp4"
with bucket.open_download_stream_by_name(filename) as grid_out:
    with open("downloaded_" + filename, "wb") as file:
        file.write(grid_out.read())
print(f"Video downloaded successfully as 'downloaded_{filename}'")

# Downloading an ISO File

filename = "linux.iso"
with bucket.open_download_stream_by_name(filename) as grid_out:
    with open("downloaded_" + filename, "wb") as file:
        file.write(grid_out.read())
print(f"ISO file downloaded successfully as 'downloaded_{filename}'")

# General Approach for Any File Type

# If you don’t know the file extension, you could:

#     Retrieve it from the metadata stored with the file, if available.
#     Use the original filename in GridFS for reference when saving locally.

# Summary

#     File Type Agnostic: GridFS handles all files as binary, so you don’t need to treat files differently based on type.
#     Save with Correct Extension: Save the downloaded file with the appropriate extension (e.g., .jpg for images, .mp4 for videos).
#     Binary Write Mode ("wb"): Always open the output file in binary mode for writing.

# This approach will allow you to download any type of file correctly from GridFS. Let me know if you have further questions!
