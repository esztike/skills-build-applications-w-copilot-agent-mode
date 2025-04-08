from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection details
DB_NAME = "octofit_db"
COLLECTION_NAME = "test_collection"

# Connect to MongoDB
print("Connecting to MongoDB...")
client = MongoClient("localhost", 27017)
db = client[DB_NAME]
print("Database name:", DB_NAME)
print("Collection name:", COLLECTION_NAME)

# Test data
test_data = {
    "_id": ObjectId(),
    "name": "Test User",
    "email": "testuser@example.com",
    "score": 100
}

# Insert test data
print("Inserting test data...")
db[COLLECTION_NAME].insert_one(test_data)

# Retrieve and print test data
print("Retrieving test data...")
retrieved_data = db[COLLECTION_NAME].find_one({"_id": test_data["_id"]})
print(retrieved_data)

# Clean up
print("Cleaning up test data...")
db[COLLECTION_NAME].delete_one({"_id": test_data["_id"]})

print("Test completed.")
