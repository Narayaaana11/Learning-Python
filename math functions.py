# Inbuilt math functions in Python
import math   # importing the math module

x = 3.14
v = -4
y = 4
z = 5

print("x =", x)
print("v =", v)
print("y =", y)
print("z =", z)
print()

# round() → rounds a number to the nearest integer
result = round(x)
print("round(x):", result)

# abs() → returns absolute (positive) value
result = abs(v)
print("abs(v):", result)

# pow(a, b) → a raised to the power b
result = pow(4, 3)
print("pow(4, 3):", result)

# max() → returns the largest value
result = max(x, y, z)
print("max(x, y, z):", result)

# min() → returns the smallest value
result = min(x, y, z)
print("min(x, y, z):", result)
print()

# math.pi → value of π
print("math.pi:", math.pi)

# math.e → value of Euler's number
print("math.e:", math.e)

# math.sqrt() → square root
result = math.sqrt(x)
print("math.sqrt(x):", result)

# math.ceil() → rounds up to nearest integer
c = 9.1
result = math.ceil(c)
print("math.ceil(9.1):", result)

# math.floor() → rounds down to nearest integer
b = 9.9
result = math.floor(b)
print("math.floor(9.9):", result)
