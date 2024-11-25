Here’s an expanded guide with commands for deleting collections and databases in MongoDB using `mongosh`:

```markdown
# Basic MongoDB `mongosh` Guide

## What is a MongoDB Document?

In MongoDB, records are called **documents**. Each document is a data structure composed of field-value pairs, where fields can hold various data types, including numbers, strings, booleans, arrays, and even nested documents.

### Example Document
```json
{
  "title": "Post Title 1",
  "body": "Body of post.",
  "category": "News",
  "likes": 1,
  "tags": ["news", "events"],
  "date": ISODate("2023-10-28T00:00:00Z")
}
```

---

## Checking `mongosh` Version

To check the version of `mongosh` installed, run:
```shell
mongosh --version
```

---

## Connecting to MongoDB

To connect to a MongoDB instance, use the `mongosh` command with host, port, and authentication details if required.

### Basic Connection Command
```shell
mongosh --host <host> --port <port> -u <username> -p <password> --authenticationDatabase <authDatabase>
```

### Example:
```shell
mongosh --host 192.168.1.19 --port 27017 -u abdi -p @abdi5520 --authenticationDatabase admin
```

---

## Common `mongosh` Commands

Once connected, you can perform various operations to manage databases, collections, and documents.

### Database Commands

- **Show Current Database**: Check which database is currently active.
  ```javascript
  db
  ```
- **Show All Databases**: List all databases.
  ```javascript
  show dbs
  ```
- **Switch or Create a Database**: Switch to or create a new database.
  ```javascript
  use databaseName
  ```
- **Delete a Database**: Delete the current database. Use with caution, as this action is irreversible.
  ```javascript
  db.dropDatabase()
  ```
  > **Note**: Make sure you are in the correct database (you can check by typing `db`) before running this command.

### Collection Commands

- **Create a Collection**: Create a new collection explicitly.
  ```javascript
  db.createCollection("collectionName")
  ```
- **Show All Collections**: List all collections in the current database.
  ```javascript
  show collections
  ```
- **Delete a Collection**: Drop a collection to remove it and all of its documents.
  ```javascript
  db.collectionName.drop()
  ```

### Document Operations

#### Insert Documents

- **Insert One Document**:
  ```javascript
  db.collectionName.insertOne({ field1: "value1", field2: "value2" })
  ```
- **Insert Multiple Documents**:
  ```javascript
  db.collectionName.insertMany([{ field1: "value1" }, { field2: "value2" }])
  ```

#### Query Documents

- **Find All Documents**: Retrieve all documents from a collection.
  ```javascript
  db.collectionName.find()
  ```
- **Find Documents with Conditions**: Use a query object to filter documents.
  ```javascript
  db.collectionName.find({ field: "value" })
  ```
- **Find One Document**: Retrieve the first document that matches the query.
  ```javascript
  db.collectionName.findOne({ field: "value" })
  ```

#### Update Documents

- **Update One Document**: Update the first matching document.
  ```javascript
  db.collectionName.updateOne({ field: "value" }, { $set: { field: "newValue" } })
  ```
- **Update Multiple Documents**: Update all documents that match the query.
  ```javascript
  db.collectionName.updateMany({ field: "value" }, { $set: { field: "newValue" } })
  ```

#### Delete Documents

- **Delete One Document**: Delete the first document that matches the query.
  ```javascript
  db.collectionName.deleteOne({ field: "value" })
  ```
- **Delete Multiple Documents**: Delete all documents that match the query.
  ```javascript
  db.collectionName.deleteMany({ field: "value" })
  ```

By using these basic commands, you can perform essential MongoDB operations directly from the `mongosh` shell, including managing databases, collections, and documents.
```