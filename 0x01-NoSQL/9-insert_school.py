#!/usr/bin/env python3
"""
A module the implements insert_school(mongo_collection, **kwargs):
"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that insert a doc in a collection
    """
    new_doc = kwargs
    result = mongo_collection.insert(new-doc)
    return result
