#!/usr/bin/env python3
"""
List all documents in Python
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
