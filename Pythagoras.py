import math  # Importing math module for sqrt() and pow()

# Taking input from the user
a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))

print("Side a entered:", a)
print("Side b entered:", b)

# Calculating side c using Pythagoras theorem
# c = √(a² + b²)
c = math.sqrt(pow(a, 2) + pow(b, 2))

# Displaying the result
print(f"Side c = {c}")
