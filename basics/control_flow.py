"""
Control Flow - Conditional Statements and Loops

This module demonstrates if/else statements, for loops, and while loops.
"""

# If-Else Statements
print("=== If-Else Statements ===")
age = 20

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# For Loops
print("\n=== For Loops ===")
fruits = ["apple", "banana", "cherry", "date"]

print("Iterating through a list:")
for fruit in fruits:
    print(f"- {fruit}")

print("\nUsing range:")
for i in range(5):
    print(f"Number: {i}")

# While Loops
print("\n=== While Loops ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break and Continue
print("\n=== Break and Continue ===")
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(f"Value: {i}")

# Nested Loops
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row
