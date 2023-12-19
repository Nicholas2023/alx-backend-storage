#!/usr/bin/env python3
"""
A module that implements list_all(mongo_collection):
"""
from typing import List


def list_all(mongo_collection: Any) -> List[Any]:
    """
    A function that lists all documents in a collection
    """
    all_doc = list(mongo_collection.find())
    return all_doc
