# variable = A container for a value string, integer, float, boolean
#            A variable behaves as if it was the value it contains

# String
firstname = "Narayana"
lastname = "Thota"
email = "narayaaana11@gmail.com"

print(firstname)
print(lastname)
print(f"firstname {firstname} lastname {lastname}")
print(f"email {email}")

# Integer
age = 23
quantity = 5

print(f"your age is {age}")
print(f"your are buying {quantity} items")

# Float
price = 5.99
cgpa = 7.84
distance = 5.5

print(f"your price is ${price}")
print(f"your cgpa is {cgpa}")
print(f"your distance is {distance}")

#boolean
is_student = True
print("are you a student?")
for_sale = True

if is_student:
    print("yes")
else:
    print("no")

if for_sale:
    print("The item is available")
