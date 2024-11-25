# from pymongo import MongoClient
# import gridfs 


# # Define MongoDB connection parameters
# host = "192.168.1.42"
# port = 27017
# username = "abdi"
# password = "abdi9006"
# auth_database = "admin"


# client = MongoClient(
#     host=host,
#     port=port,
#     username=username,
#     password=password,
#     authSource= auth_database
# )

# db = client["myfiles"]

# # Create a GridFS bucket within the database
# bucket = gridfs.GridFSBucket(db)


# '''
# Uploading an Existing File: To upload an existing file (like a .txt, .pdf, or .jpg file), we use upload_from_stream(). This method will take the file and automatically split it into chunks before storing it in GridFS.
# '''


# with open('n6obp6en1yv61.jpg', "rb") as file:
#     file_id = bucket.upload_from_stream(
#         "n6obp6en1yv61.jpg",
#         file,
#         chunk_size_bytes=1048576,  # Optional: Set chunk size to 1 MB        
#         metadata={"contentType": "iso"}  # Optional: Add metadata
         
#     )
# print("File uploaded successfully with ID:", file_id)


# '''
# Uploading an Existing File: To upload an existing file (like a .txt, .pdf, or .jpg file), we use upload_from_stream(). This method will take the file and automatically split it into chunks before storing it in GridFS.


# Filename: "file.txt" will be the name of the file in GridFS.
# File Object: file is the file object read in binary mode.
# Chunk Size: Set to 1 MB here (you can adjust as needed).
# Metadata: Custom data (like file type or description) stored with the file.
# '''


from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import gridfs
from bson import ObjectId
import io

app = FastAPI()

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection details
host = "192.168.1.42"
port = 27017
username = "abdi"
password = "abdi9006"
auth_database = "admin"

# Connect to MongoDB
client = MongoClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource=auth_database
)

# Database and GridFSBucket setup
db = client["myfiles"]
bucket = gridfs.GridFSBucket(db)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file to GridFS using GridFSBucket.
    """
    try:
        # Read file content
        content = await file.read()
        
        # Upload file to GridFSBucket
        file_id = bucket.upload_from_stream(
            file.filename,
            io.BytesIO(content),  # Stream-like object
            metadata={"contentType": file.content_type}
        )

        return JSONResponse(content={"file_id": str(file_id), "filename": file.filename})

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to upload file")

@app.get("/file/{file_id}")
async def get_file(file_id: str):
    """
    Retrieve a file by ID from GridFS using GridFSBucket and serve it.
    """
    try:
        # Retrieve file from GridFSBucket by ID
        grid_out = bucket.open_download_stream(ObjectId(file_id))

        # Stream the file content using FastAPI's StreamingResponse
        return StreamingResponse(
            grid_out,
            media_type=grid_out.metadata.get("contentType", "application/octet-stream"),
            headers={"Content-Disposition": f"attachment; filename={grid_out.filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/files")
async def list_files():
    """
    List all files in the GridFS.
    """
    try:
        files = []
        for file in bucket.find():
            files.append({
                "file_id": str(file._id),
                "filename": file.filename
            })
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve file list")
