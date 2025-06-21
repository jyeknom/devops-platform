from pymongo import MongoClient
import os

MONGO_URL = os.getenv('MONGO_URL', 'mongodb://mongodb:27017')
client = MongoClient(MONGO_URL)
db = client["devops"]
