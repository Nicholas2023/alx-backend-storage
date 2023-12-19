#!/usr/bin/env python3
"""
A module that implements list_all(mongo_collection):
"""


def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    A function that lists all documents in a collection
    """
    return [doc for doc in mongo_collection.find()]
