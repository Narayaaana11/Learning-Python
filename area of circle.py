import math  # Importing math module for pi

# Taking radius input from the user
radius = float(input("Enter the radius of the circle: "))

print("Radius entered:", radius)

# Formula for area of a circle: π × r²
area = math.pi * pow(radius, 2)

# Printing the area rounded to 2 decimal places
print(f"The area of the circle is: {round(area, 2)} cm^2")
