"""
Decorators in Python

This module demonstrates how to create and use decorators.
Decorators are a powerful feature that allows you to modify or enhance functions.
"""

import time
import functools

# Basic Decorator
def simple_decorator(func):
    """A simple decorator that prints before and after function execution"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# Decorator with Arguments
def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

# Timing Decorator
def timer(func):
    """Decorator to measure function execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """A function that takes some time to execute"""
    time.sleep(1)
    return "Done!"

# Class-based Decorator
class CountCalls:
    """Decorator that counts how many times a function is called"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

# Main execution
if __name__ == "__main__":
    print("=== Basic Decorator ===")
    say_hello()
    
    print("\n=== Decorator with Arguments ===")
    greet("Alice")
    
    print("\n=== Timing Decorator ===")
    result = slow_function()
    print(f"Result: {result}")
    
    print("\n=== Class-based Decorator ===")
    say_hi()
    say_hi()
    say_hi()
    print(f"Total calls: {say_hi.count}")
