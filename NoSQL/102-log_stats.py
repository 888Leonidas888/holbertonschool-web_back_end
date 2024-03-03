#!/usr/bin/env python3
"""Nueva versión de estadística de ngnix"""


from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client['logs']['nginx']

    total_documents = collection.count_documents({})
    total_status = collection.count_documents({"path": "/status"})

    methods = [
        {"method": "GET"},
        {"method": "POST"},
        {"method": "PUT"},
        {"method": "PATCH"},
        {"method": "DELETE"},
    ]

    totales = [collection.count_documents(method) for method in methods]

    print(f'{total_documents} logs')
    print('Methods:')
    for i, t in enumerate(totales):
        print(f'\tmethod {methods[i].get("method")}: {t}')
    print(f'{total_status} status check')

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ips = collection.aggregate(pipeline)

    print('IPs:')
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
