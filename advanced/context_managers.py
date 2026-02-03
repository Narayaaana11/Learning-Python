"""
Context Managers in Python

This module demonstrates how to use and create context managers.
Context managers handle setup and cleanup automatically using 'with' statements.
"""

import os
from contextlib import contextmanager

# Using built-in context manager
print("=== Built-in Context Manager (File) ===")

# Writing to a file
with open('/tmp/example.txt', 'w') as f:
    f.write("Hello, Context Manager!")
    print("File written successfully")
# File is automatically closed here

# Reading from a file
with open('/tmp/example.txt', 'r') as f:
    content = f.read()
    print(f"File content: {content}")

# Custom Context Manager using Class
class DatabaseConnection:
    """Simulates a database connection context manager"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        # Return False to propagate exceptions, True to suppress
        return False

print("\n=== Custom Context Manager (Class) ===")
with DatabaseConnection("my_database") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")

# Custom Context Manager using Generator
@contextmanager
def temporary_directory(dir_name):
    """Create and cleanup a temporary directory"""
    print(f"Creating directory: {dir_name}")
    os.makedirs(dir_name, exist_ok=True)
    try:
        yield dir_name
    finally:
        print(f"Cleaning up directory: {dir_name}")
        if os.path.exists(dir_name):
            os.rmdir(dir_name)

print("\n=== Custom Context Manager (Generator) ===")
with temporary_directory("/tmp/temp_dir") as temp_dir:
    print(f"Working in {temp_dir}")
    print("Directory exists:", os.path.exists(temp_dir))
print("Directory exists after context:", os.path.exists("/tmp/temp_dir"))

# Multiple Context Managers
print("\n=== Multiple Context Managers ===")
with open('/tmp/source.txt', 'w') as source, \
     open('/tmp/dest.txt', 'w') as dest:
    source.write("Source content")
    dest.write("Destination content")
    print("Both files written")

# Cleanup
os.remove('/tmp/example.txt')
os.remove('/tmp/source.txt')
os.remove('/tmp/dest.txt')
print("\n=== Cleanup complete ===")
