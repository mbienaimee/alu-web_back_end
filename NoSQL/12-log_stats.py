#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

from pymongo import MongoClient

def nginx_log_stats():
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    
    # Ensure collection is not empty
    if nginx_collection.estimated_document_count() == 0:
        print('0 logs')
        print('Methods:')
        print('\tmethod GET: 0')
        print('\tmethod POST: 0')
        print('\tmethod PUT: 0')
        print('\tmethod PATCH: 0')
        print('\tmethod DELETE: 0')
        print('0 status check')
        return
    
    # Count total logs
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')
    
    # Count logs by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    
    # Count logs with method GET and path /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

if __name__ == "__main__":
    nginx_log_stats()
