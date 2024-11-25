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
You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

'''
try:
    schoolDB = client["school"]
    studentColl = schoolDB["students"]
    coursesColl = schoolDB["courses"]

    '''
    The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
    '''
    coursesColl.drop()

except Exception as e:
    print("Error has occured", e)