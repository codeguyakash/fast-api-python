from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client["fast-api-python"]

user_collection = db["users"]