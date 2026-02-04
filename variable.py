# variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it were the value it contains

# ---------- String ----------
first_name = "Narayana"
last_name = "Thota"
email = "narayaaana11@gmail.com"

print("First name:", first_name)
print("Last name:", last_name)
print(f"Full name: {first_name} {last_name}")
print(f"Email: {email}")
print()

# ---------- Integer ----------
age = 23
quantity = 5

print(f"Your age is {age}")
print(f"You are buying {quantity} items")
print()

# ---------- Float ----------
price = 5.99
cgpa = 7.84
distance = 5.5

print(f"Price: ${price}")
print(f"CGPA: {cgpa}")
print(f"Distance: {distance}")
print()

# ---------- Boolean ----------
is_student = True
for_sale = True

print("Are you a student?")
if is_student:
    print("Yes")
else:
    print("No")

if for_sale:
    print("The item is available for sale")
else:
    print("The item is not available")
