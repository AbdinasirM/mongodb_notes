from motor.motor_asyncio import AsyncIOMotorClient
from typing import Union
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI

# Define MongoDB connection parameters
host = "192.168.1.19"
port = 27017
username = "abdi"
password = "@abdi5520"
auth_database = "admin"

client = AsyncIOMotorClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource=auth_database
)



#User profile model
class Users(BaseModel):
    name: str
    age: int

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
async def createUserProfile(users: Users):

    ins = await userCollection.insert_one({"name": users.name, "age": users.age})

    return F"{ins.inserted_id}, It has been saved"


@app.post('/userinfo')
async def getUserInfo(users: Users):
    
    userinfo = await userCollection.find({"name": {"$eq":users.name}}, {"_id":0}).to_list(length=None)
    
    return {"user_info": userinfo}


@app.delete('/deleteuser')
async def deleteUser(users:Users):
    
    userQuery = {
        "name":users.name
    }
    userExists = userCollection.find_one(userQuery)
    if userExists:
        deletedUser = await userCollection.delete_one(userQuery)
        return {"Deleted user count": deletedUser.deleted_count}
    else:
        return {"error": "User not found"}
    

@app.put('/updateuser')
async def updateUser(users: Users):
    userprofile = client["userDB"]
    userCollection = userprofile["users"]

    userQuery = {"name": users.name}  # Locate the user by name
    update_values = {"$set": {"age": users.age}}  # Define fields to update

    userExists = await userCollection.find_one(userQuery)  # Check if user exists
    if userExists:
        updatedUser = await userCollection.update_one(userQuery, update_values)  # Pass both filter and update
        return {"Updated user count": updatedUser.modified_count}
    else:
        return {"Error": "User not found"}
