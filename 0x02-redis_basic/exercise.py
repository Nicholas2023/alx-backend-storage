#!/usr/bin/env python3
"""
A module that implemts class Cache()
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A class for interacting with redis as a data cache
    """
    def __init__(self):
        """
        Initializes a Redis connection and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis with a generated random key
        Args:
            - data (Union[Any]) data to be stored in Redis
        Returns:
            - str: The generated random key used for storing the data
        """

        key = str(uuid.uuid4())  # Gen rand. key
        self._redis.set(key, data)  # Stores data
        return key
