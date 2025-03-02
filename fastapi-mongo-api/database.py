
# database.py
from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

def get_db():
    client = MongoClient(mongodb+srv://rishabhtrivedi:<RaNULHVbm2RIPoad>@fastapi.tcdpj.mongodb.net/?retryWrites=true&w=majority&appName=FASTAPI)
    db = client[mongodbVSCodePlaygroundDB]
    return db
