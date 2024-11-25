Here’s the improved content in Markdown format for MongoDB Query Operators:

```markdown
# MongoDB Query Operators

MongoDB provides a variety of query operators to compare and reference document fields. These operators can be categorized into **Comparison**, **Logical**, and **Evaluation** operators.

---

## Comparison Operators

Comparison operators allow you to match documents based on the comparison of field values.

- **`$eq`**: Matches documents where the field value is equal to the specified value.
- **`$ne`**: Matches documents where the field value is not equal to the specified value.
- **`$gt`**: Matches documents where the field value is greater than the specified value.
- **`$gte`**: Matches documents where the field value is greater than or equal to the specified value.
- **`$lt`**: Matches documents where the field value is less than the specified value.
- **`$lte`**: Matches documents where the field value is less than or equal to the specified value.
- **`$in`**: Matches documents where the field value is in the specified array of values.

**Example:**
```javascript
db.collection.find({ age: { $gte: 18 } })
```

---

## Logical Operators

Logical operators allow you to combine multiple conditions in a query.

- **`$and`**: Returns documents that match both conditions.
- **`$or`**: Returns documents that match either of the conditions.
- **`$nor`**: Returns documents that fail to match both conditions.
- **`$not`**: Returns documents that do not match the specified condition.

**Example:**
```javascript
db.collection.find({
  $and: [
    { age: { $gte: 18 } },
    { status: "active" }
  ]
})
```

---

## Evaluation Operators

Evaluation operators provide advanced matching capabilities, such as regular expressions and JavaScript expressions.

- **`$regex`**: Allows pattern matching using regular expressions.
- **`$text`**: Performs a full-text search on a field with a text index.
- **`$where`**: Uses a JavaScript expression to match documents based on a custom condition.

**Example using `$regex`:**
```javascript
db.collection.find({ name: { $regex: /^A/ } })
```

**Example using `$where`:**
```javascript
db.collection.find({ $where: "this.age > 18" })
```

---

By using these operators, MongoDB queries become highly flexible and powerful, allowing for complex data retrieval based on conditions across various fields.
```