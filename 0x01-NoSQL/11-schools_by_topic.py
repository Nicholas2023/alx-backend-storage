#!/usr/bin/env python3
"""
A module that implements schools_by_topic(mongo_collection, topic):
"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that returns the list of documents having
    specific topics
    """
    schools = {
        "topics": {
            "$elemMatch": {
                "$eq": topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(schools)]
