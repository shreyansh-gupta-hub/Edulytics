from pymongo import MongoClient
import os

client = MongoClient(os.getenv('mongodb+srv://shreyanshgupta:wiwmat-vissA6-tipdyc@cluster0.ag5a91z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
db = client['student_db']
collection = db['students']

def save_data_to_mongo(data_dict):
    collection.insert_many(data_dict)