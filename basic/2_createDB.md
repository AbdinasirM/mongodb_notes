Here’s the improved content in Markdown format:

```markdown
# MongoDB `mongosh` Database and Collection Operations

## Creating and Managing Databases in `mongosh`

### View the Current Database
After connecting to MongoDB using `mongosh`, you can check which database you’re currently using by typing:
```javascript
db
```

### Show All Databases
To list all available databases, use:
```javascript
show dbs
```

### Change or Create a New Database
To switch to a different database or create a new one, use the `use` command followed by the database name:
```javascript
use databaseName
```
> If the specified database does not exist, MongoDB will create it once data is added to it.

---

## Creating Collections in `mongosh`

There are two primary ways to create a collection in MongoDB.

### Method 1: Using `createCollection()`
You can create a new collection explicitly with the `createCollection()` method.
```javascript
db.createCollection("test")
```

### Method 2: Automatic Creation via Insert
MongoDB can also create a collection automatically when you first insert data into it.

Example:
```javascript
const document = { name: "Abdi" }
db.Tuts.insertOne(document)
```

---

## Inserting Documents in `mongosh`

MongoDB provides two main methods for inserting documents into a collection: `insertOne()` and `insertMany()`.

### Using `insertOne()`
To insert a single document, use the `insertOne()` method. This method adds one object into the collection.

**Example:**
```javascript
db.Tuts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: new Date()
})
```
> Note: If the collection doesn’t exist yet, MongoDB will automatically create it during the insert operation.

### Using `insertMany()`
To insert multiple documents at once, use the `insertMany()` method. This method takes an array of objects.

**Example:**
```javascript
db.Tuts.insertMany([
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: new Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: new Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: new Date()
  }
])
```

By following these steps, you can easily create and manage databases, collections, and documents in MongoDB using `mongosh`.
```