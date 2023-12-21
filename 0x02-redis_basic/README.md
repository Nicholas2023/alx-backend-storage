# Redis Basic Operations in Python :smile:

This repository contains Python code implementing a `Cache` class that utilizes Redis for storing and managing data. The `Cache` class gradually extends its functionality across multiple tasks, enhancing its capabilities.

## Tasks Overview

### 1. Writing strings to Redis
- Create a `Cache` class with an initialized Redis client and a method to store data in Redis.

### 2. Reading from Redis and recovering original type
- Implement a `get` method to retrieve data from Redis with optional type conversion functions.
- Additional methods like `get_str` and `get_int` facilitate specific type retrieval.

### 3. Incrementing values
- Implement a `count_calls` decorator to count method calls in the `Cache` class.

### 4. Storing lists
- Create a `call_history` decorator to store input/output history for specific functions.

### 5. Retrieving lists
- Implement a `replay` function to display the history of calls for a specific function.

### 6. Implementing an expiring web cache and tracker (Advanced)
- Create a `get_page` function to fetch web page content, tracking URL accesses and caching results with a time expiration.

## Repository Structure

The repository contains the following structure:

```
- /0x02-redis_basic
  - exercise.py      # Contains the Cache class and methods for Redis operations
  - main.py          # Examples demonstrating the implemented functionalities
  - README.md        # Documentation file (you're reading this!)
```

## Usage

To use this code:

1. Clone the repository.
2. Install the required dependencies.
3. Run the individual Python files (`main.py`) to see the functionalities in action.

## Dependencies

- Python 3.x
- `redis` Python package

## Resources

- [Redis Documentation](https://redis.io/documentation)
- [Python Redis Package](https://redis-py.readthedocs.io/)

## Contributors

- Nicholas Otieno

Feel free to contribute by forking this repository and submitting pull requests.
