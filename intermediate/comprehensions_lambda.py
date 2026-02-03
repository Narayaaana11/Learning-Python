"""
List Comprehensions and Lambda Functions

This module demonstrates list comprehensions, dictionary comprehensions,
and lambda functions - powerful Python features for concise code.
"""

# List Comprehensions
print("=== List Comprehensions ===")

# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table:\n{matrix}")

# Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")

# Create a dictionary of squares
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dictionary: {square_dict}")

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Set Comprehensions
print("\n=== Set Comprehensions ===")
unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
print(f"Unique word lengths: {unique_lengths}")

# Lambda Functions
print("\n=== Lambda Functions ===")

# Basic lambda
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda with sorted
words = ["python", "is", "awesome", "and", "fun"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {sorted_by_length}")

# Combining techniques
print("\n=== Combining Techniques ===")

# List of dictionaries with comprehension and lambda
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age using lambda
sorted_people = sorted(people, key=lambda x: x["age"])
print("Sorted by age:")
for person in sorted_people:
    print(f"  {person['name']}: {person['age']}")

# Extract names using comprehension
names = [person["name"] for person in people if person["age"] >= 30]
print(f"Names of people 30 or older: {names}")
