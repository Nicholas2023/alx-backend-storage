# NoSQL - MongoDB and Python Scripting :smile:

This repository contains a set of scripts and Python functions designed to interact with MongoDB, perform various operations, and manipulate data.

## Project Structure

- `0-list_databases`: Script listing all databases in MongoDB.
- `1-use_or_create_database`: Script creating or using the database `my_db`.
- `2-insert`: Script inserting a document into the `school` collection.
- `3-all`: Script listing all documents in the `school` collection.
- `4-match`: Script listing documents with name="Holberton school" in the `school` collection.
- `5-count`: Script displaying the number of documents in the `school` collection.
- `6-update`: Script adding a new attribute to a document in the `school` collection.
- `7-delete`: Script deleting all documents with name="Holberton school" in the `school` collection.
- `8-all.py`: Python function to list all documents in a collection.
- `9-insert_school.py`: Python function to insert a new document in a collection based on kwargs.
- `10-update_topics.py`: Python function to change all topics of a school document based on the name.
- `11-schools_by_topic.py`: Python function to retrieve a list of schools having a specific topic.
- `12-log_stats.py`: Python script providing statistics about Nginx logs stored in MongoDB.
- `100-find`: Script listing all documents with name starting by Holberton in the collection `school`.
- `101-students.py`: Python function to return all students sorted by average score.
- `102-log_stats.py`: Improved version of `12-log_stats.py` with additional statistics about IPs.

## How to Use

### Requirements

- MongoDB installed and running.
- Python environment with `pymongo` library.

### Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/alx-backend-storage.git
   ```

2. Run MongoDB.

3. Execute the scripts or import the Python functions as needed:
   ```bash
   python <script_name>.py
   ```

## Additional Notes

- The Python scripts require appropriate permissions and configurations to connect to the MongoDB instance.
- For detailed information on each script/function, refer to their respective file or code comments.
```
