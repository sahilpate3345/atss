import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Default to localhost if not set, but user should set this in .env
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "ats_hiring_db")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Trigger a connection to verify
    client.server_info()
    print(f"Connected to MongoDB: {DB_NAME}")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

db = client[DB_NAME]

def get_db():
    return db
