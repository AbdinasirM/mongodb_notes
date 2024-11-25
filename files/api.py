from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import gridfs
from bson import ObjectId
import io
from datetime import datetime

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
password = "abdi06"
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
        
        # Upload file to GridFSBucket with metadata
        file_id = bucket.upload_from_stream(
            file.filename,
            io.BytesIO(content),
            metadata={
                "contentType": file.content_type,
                "uploadDate": datetime.utcnow()
            }
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
        grid_out = bucket.open_download_stream(ObjectId(file_id))
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
    List all files in the GridFS with metadata and upload date.
    """
    try:
        files = []
        for file in bucket.find():
            files.append({
                "file_id": str(file._id),
                "filename": file.filename,
                "contentType": file.metadata.get("contentType", "application/octet-stream"),
                "uploadDate": file.upload_date.isoformat() if file.upload_date else "Unknown",
                "metadata": file.metadata
            })
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve file list")

@app.put("/file/{file_id}/rename")
async def rename_file(file_id: str, new_filename: str):
    """
    Rename a file in GridFS by file ID.
    """
    try:
        bucket.rename(ObjectId(file_id), new_filename)
        return JSONResponse(content={"file_id": file_id, "new_filename": new_filename})
    except Exception as e:
        raise HTTPException(status_code=404, detail="File not found or rename failed")

@app.delete("/file/{file_id}")
async def delete_file(file_id: str):
    """
    Delete a file from GridFS by file ID.
    """
    try:
        bucket.delete(ObjectId(file_id))
        return JSONResponse(content={"file_id": file_id, "status": "deleted"})
    except Exception as e:
        raise HTTPException(status_code=404, detail="File not found or delete failed")
