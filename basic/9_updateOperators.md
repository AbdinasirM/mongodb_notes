Here’s the improved content in Markdown format for MongoDB Update Operators:

```markdown
# MongoDB Update Operators

MongoDB provides a variety of update operators to modify document fields and arrays during update operations. These operators are divided into categories based on their functionality.

---

## Field Update Operators

These operators allow you to update or modify individual fields in documents.

- **`$currentDate`**: Sets the field value to the current date.
- **`$inc`**: Increments the field value by a specified amount.
- **`$rename`**: Renames a field in the document.
- **`$set`**: Sets the value of a field, adding it if it doesn’t exist.
- **`$unset`**: Removes the field from the document.

**Example:**
```javascript
db.collection.updateOne(
  { title: "Post Title 1" },
  {
    $set: { views: 100 },
    $inc: { likes: 1 },
    $currentDate: { lastUpdated: true }
  }
)
```

In this example, we set the `views` field to `100`, increment `likes` by `1`, and update `lastUpdated` to the current date.

---

## Array Update Operators

These operators are specifically for modifying arrays within documents.

- **`$addToSet`**: Adds a unique element to an array (only if it doesn’t already exist in the array).
- **`$pop`**: Removes the first or last element of an array (`1` for the last element, `-1` for the first).
- **`$pull`**: Removes all elements in an array that match a specified condition.
- **`$push`**: Adds an element to the end of an array.

**Example:**
```javascript
db.collection.updateOne(
  { title: "Post Title 1" },
  {
    $push: { tags: "newTag" },
    $addToSet: { tags: "uniqueTag" },
    $pop: { tags: 1 },
    $pull: { tags: "oldTag" }
  }
)
```

In this example:
- `$push` adds `"newTag"` to the end of the `tags` array.
- `$addToSet` adds `"uniqueTag"` only if it doesn’t already exist in `tags`.
- `$pop` removes the last element of `tags`.
- `$pull` removes `"oldTag"` from `tags`.

---

## Example Aggregation with `$push`

Here’s an example of using `$push` in an aggregation pipeline to group properties by `property_type` and store the results in a new collection.

**Example:**
```javascript
db.listingsAndReviews.aggregate([
  {
    $group: {
      _id: "$property_type",
      properties: {
        $push: {
          name: "$name",
          accommodates: "$accommodates",
          price: "$price"
        }
      }
    }
  },
  { $out: "properties_by_type" }
])
```

In this aggregation:
- We group documents by `property_type` and use `$push` to gather `name`, `accommodates`, and `price` fields into the `properties` array.
- The `$out` stage writes the results to a new collection called `properties_by_type`.

---

These update operators allow you to manipulate both fields and arrays efficiently, providing powerful tools for modifying documents in MongoDB.
```