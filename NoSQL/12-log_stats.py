#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx
logs stored in MongoDB
"""


import pymongo
from pymongo import MongoClient


def nginx_stats(mongo_collection):
    """gives some stats about Nginx logs"""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    get_nums = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{get_nums} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_stats(mongo_collection)
