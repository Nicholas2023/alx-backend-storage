#!/usr/bin/env python3
"""
A module that implements schools_by_topic(mongo_collection, topic):
"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that returns the list of documents having
    specific topics
    """
    schools = mongo_collection.find({"topic": topic})
    return list(schools)
