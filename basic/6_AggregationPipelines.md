Here's the content in a Markdown file format:

```markdown
# Aggregation Pipelines in MongoDB

Aggregation operations in MongoDB allow you to group, sort, perform calculations, and analyze data in a flexible way.

An aggregation pipeline can have one or more **stages**, where each stage processes the output of the previous stage. The order of stages is crucial for achieving the desired result.

## Basic Example
```javascript
db.posts.aggregate([
  // Stage 1: Filter documents with more than 1 like
  { $match: { likes: { $gt: 1 } } },
  // Stage 2: Group by category and sum likes
  { $group: { _id: "$category", totalLikes: { $sum: "$likes" } } }
])
```

**Result:**
```plaintext
[
  { _id: 'Event', totalLikes: 6 },
  { _id: 'Technology', totalLikes: 3 }
]
```

---

## Aggregation Stages

### 1. `$group`

The `$group` stage groups documents by a specified `_id` expression, which doesn’t have to be the document’s original `_id` field. 

```javascript
db.mycol.aggregate([{ $group: { _id: "$property_type" } }])
```

This returns distinct values of the `property_type` field.

### 2. `$limit`

The `$limit` stage restricts the number of documents that pass to the next stage.

**Example:**
```javascript
db.mycol.aggregate([{ $limit: 1 }])
```

### 3. `$project`

The `$project` stage specifies which fields to pass to the next stage, similar to the projection in `find()` queries.

```javascript
db.mycol.aggregate([
  {
    $project: {
      name: 1,
      cuisine: 1,
      address: 1
    }
  },
  { $limit: 5 }
])
```

This will only return the `name`, `cuisine`, and `address` fields for the first 5 documents.

### 4. `$sort`

The `$sort` stage sorts documents in the specified order. Use `1` for ascending order and `-1` for descending.

```javascript
db.listingsAndReviews.aggregate([
  { $sort: { accommodates: -1 } },
  {
    $project: { name: 1, accommodates: 1 }
  },
  { $limit: 5 }
])
```

This example sorts documents by the `accommodates` field in descending order, displaying only `name` and `accommodates` fields for the first 5 documents.

### 5. `$match`

The `$match` stage filters documents based on specified criteria, similar to a `find` query. Placing `$match` early in the pipeline can improve performance.

```javascript
db.listingsAndReviews.aggregate([
  { $match: { property_type: "House" } },
  { $limit: 2 },
  {
    $project: { name: 1, bedrooms: 1, price: 1 }
  }
])
```

This example returns documents where `property_type` is `"House"`.

### 6. `$addFields`

The `$addFields` stage adds new fields to documents.

```javascript
db.restaurants.aggregate([
  {
    $addFields: { avgGrade: { $avg: "$grades.score" } }
  },
  {
    $project: { name: 1, avgGrade: 1 }
  },
  { $limit: 5 }
])
```

### 7. `$count`

The `$count` stage counts the number of documents in the pipeline.

```javascript
db.restaurants.aggregate([
  { $match: { cuisine: "Chinese" } },
  { $count: "totalChinese" }
])
```

This example counts the number of documents with `cuisine` equal to `"Chinese"`.

### 8. `$lookup`

The `$lookup` stage performs a left outer join with another collection in the same database.

**Collections:**

**students**
```json
[
  { "_id": 1, "name": "Alice", "course_id": 101 },
  { "_id": 2, "name": "Bob", "course_id": 102 },
  { "_id": 3, "name": "Charlie", "course_id": 101 }
]
```

**courses**
```json
[
  { "_id": 101, "title": "Mathematics" },
  { "_id": 102, "title": "History" }
]
```

**Example:**
```javascript
db.students.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "course_id",
      foreignField: "_id",
      as: "course_details"
    }
  },
  { $limit: 3 }
])
```

**Result:**
```json
[
  {
    "_id": 1,
    "name": "Alice",
    "course_id": 101,
    "course_details": [{ "_id": 101, "title": "Mathematics" }]
  },
  {
    "_id": 2,
    "name": "Bob",
    "course_id": 102,
    "course_details": [{ "_id": 102, "title": "History" }]
  },
  {
    "_id": 3,
    "name": "Charlie",
    "course_id": 101,
    "course_details": [{ "_id": 101, "title": "Mathematics" }]
  }
]
```

### 9. `$out`

The `$out` stage writes the result of the aggregation pipeline to a new or existing collection. It must be the last stage of the pipeline.

---

These stages enable powerful data transformations and aggregations in MongoDB. By combining stages, you can efficiently manipulate and analyze data.
```