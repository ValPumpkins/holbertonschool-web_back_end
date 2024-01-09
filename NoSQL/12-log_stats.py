#!/usr/bin/env python3
""" Script that provides stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    """ Script that provides stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')

    database = client.logs
    collection = database.nginx

    count_logs = collection.count_documents({})

    all_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{count_logs} logs")
    print("Methods:")

    for method in all_methods:
        count_methods = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_methods}")

    result = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{result} status check")
