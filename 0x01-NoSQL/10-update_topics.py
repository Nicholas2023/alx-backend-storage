#!/usr/bin/env python3
"""
A module that implements update_topics(mongo_collection, name, topics)
"""


def update_topics(mongo_collection, name, topics):
    """
    A function that updates documents in a collection
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
