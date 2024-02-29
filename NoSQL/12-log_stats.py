#!/usr/bin/env python3
"""Muestra las estadísticas de la base de datos logs"""

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    total_documents = collection.count_documents({})
    total_get = collection.count_documents({"method": "GET"})
    total_post = collection.count_documents({"method": "POST"})
    total_put = collection.count_documents({"method": "PUT"})
    total_patch = collection.count_documents({"method": "PATCH"})
    total_delete = collection.count_documents({"method": "DELETE"})
    total_status = collection.count_documents({"path": "/status"})

    print(f'{total_documents} logs')
    print('Methods:')
    print(f'\tmethod GET: {total_get}')
    print(f'\tmethod POST: {total_post}')
    print(f'\tmethod PUT: {total_put}')
    print(f'\tmethod PATCH: {total_patch}')
    print(f'\tmethod DELETE: {total_delete}')
    print(f'{total_status} status check')
