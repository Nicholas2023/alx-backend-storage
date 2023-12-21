#!/usr/bin/env python3
"""
A module that implemts class Cache()
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) ->
    Union[str, bytes, int, float]:
        """
        Retrieves data from Redis based on the provided key
        Args:
            - key (str): The key associated with the data
            - fn (Callable): Optional conversion function
        Returns:
            - Union[Any]: The retrieved data
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis associated with the prvided
        key and converts it into a string
        Args:
            - key (str): The key associated with the data in Redis
        Returns:
            - Union[str, None]: The retrieved data converted to str
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis associated with the key
        and converts it into an int
        Args:
            - key (str): The key associated with the data
        return
            - Union[int, None]: Retrieved data converted into an int
        """
        return self.get(key, lambda d: int(d))
