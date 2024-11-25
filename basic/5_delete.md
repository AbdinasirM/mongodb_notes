Here’s the improved content in Markdown format for the deletion section:

```markdown
# MongoDB `mongosh` Delete Operations

## Deleting Documents in MongoDB

MongoDB provides two primary methods to delete documents from a collection: `deleteOne()` and `deleteMany()`. Both methods accept a **query object** to identify which documents to delete.

---

### Using `deleteOne()`

The `deleteOne()` method deletes **only the first document** that matches the provided query.

**Example:**
```javascript
db.posts.deleteOne({ title: "Post Title 5" })
```

> In this example, MongoDB will search for a document with the title `"Post Title 5"` and delete the first match it finds.

---

### Using `deleteMany()`

The `deleteMany()` method deletes **all documents** that match the provided query.

**Example:**
```javascript
db.posts.deleteMany({ category: "Technology" })
```

> In this example, all documents where the `category` is `"Technology"` will be deleted.

---

By using `deleteOne()` and `deleteMany()`, you can selectively remove documents from your MongoDB collections based on specific criteria.
```