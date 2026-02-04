# Circumference of a Circle
import math  # Importing math module for pi

# Taking radius input from the user
radius = float(input("Enter the radius of the circle: "))

print("Radius entered:", radius)

# Formula for circumference of a circle: 2 × π × r
circumference = 2 * math.pi * radius

# Printing the result rounded to 2 decimal places
print(f"Circumference of the circle: {round(circumference, 2)}")
