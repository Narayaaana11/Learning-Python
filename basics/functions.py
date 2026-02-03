"""
Functions in Python

This module demonstrates how to define and use functions in Python.
"""

# Basic Function
def greet():
    """A simple function that prints a greeting"""
    print("Hello from a function!")

# Function with Parameters
def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

# Function with Return Value
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

# Function with Default Parameters
def greet_with_title(name, title="Mr."):
    """Greet a person with a title"""
    return f"Hello, {title} {name}!"

# Function with Multiple Return Values
def get_min_max(numbers):
    """Return minimum and maximum values from a list"""
    return min(numbers), max(numbers)

# Function with *args (variable arguments)
def sum_all(*args):
    """Sum all arguments"""
    return sum(args)

# Function with **kwargs (keyword arguments)
def print_info(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Main execution
if __name__ == "__main__":
    print("=== Basic Function ===")
    greet()
    
    print("\n=== Function with Parameters ===")
    greet_person("Alice")
    
    print("\n=== Function with Return Value ===")
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    print("\n=== Function with Default Parameters ===")
    print(greet_with_title("Smith"))
    print(greet_with_title("Smith", "Dr."))
    
    print("\n=== Multiple Return Values ===")
    numbers = [4, 2, 9, 1, 7]
    minimum, maximum = get_min_max(numbers)
    print(f"Min: {minimum}, Max: {maximum}")
    
    print("\n=== Variable Arguments (*args) ===")
    print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
    
    print("\n=== Keyword Arguments (**kwargs) ===")
    print_info(name="John", age=30, city="New York")
