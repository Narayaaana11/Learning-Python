# Typecasting = The process of converting a variable's data type into another data type
#               str(), int(), float(), bool()

# Original variables
name = "narayaaana"
age = 23
cgpa = 7.84
is_student = True

print("Before typecasting:")
print("age:", age, type(age))
print("cgpa:", cgpa, type(cgpa))
print()

# Typecasting
cgpa = int(cgpa)   # float → int
age = str(age)     # int → string

print("After typecasting:")
print("cgpa:", cgpa, type(cgpa))
print("age:", age, type(age))
