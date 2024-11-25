Here’s the improved content in Markdown format for Indexing & Search:

```markdown
# Indexing & Search in MongoDB

Indexes in MongoDB are used to optimize search operations, making queries more efficient. You can create text indexes to enable full-text search capabilities on string fields.

---

## Creating a Text Index

To create a text index on a field, use the `createIndex()` method. This example creates a text index on the `title` field in the `movies` collection.

**Example:**
```javascript
db.movies.createIndex({ title: "text" })
```

The index name will be displayed as `title_text`.

---

## Performing a Text Search

Once a text index is created, you can perform a full-text search using the `$text` operator within the `find()` method. The `$search` field specifies the search keywords.

**Example:**
```javascript
db.movies.find(
  { $text: { $search: "star wars" } },
  { title: 1, year: 1 }
)
```

**Result:**
```json
[
  {
    "_id": ObjectId("67204561564530cc83fe6914"),
    "title": "Star Wars: Episode VI - Return of the Jedi",
    "year": 1983
  },
  {
    "_id": ObjectId("67204561564530cc83fe6912"),
    "title": "Star Wars: Episode IV - A New Hope",
    "year": 1977
  },
  {
    "_id": ObjectId("67204561564530cc83fe6913"),
    "title": "Star Wars: Episode V - The Empire Strikes Back",
    "year": 1980
  }
]
```

> In this example, MongoDB searches for documents containing the keywords `"star wars"` in the `title` field and returns the `title` and `year` fields for each matching document.

---

By using text indexes and `$text` search, MongoDB enables efficient searching and filtering of text-based data in collections.
```