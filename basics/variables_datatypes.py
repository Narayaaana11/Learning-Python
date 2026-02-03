"""
Variables and Data Types in Python

This module demonstrates the basic data types in Python and how to work with variables.
"""

# Numeric Types
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print("=== Numeric Types ===")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# String Type
text = "Hello, Python!"
multiline_text = """This is a
multiline string"""

print("\n=== String Type ===")
print(f"String: {text}, Type: {type(text)}")
print(f"Length: {len(text)}")

# Boolean Type
is_learning = True
is_expert = False

print("\n=== Boolean Type ===")
print(f"Is Learning: {is_learning}, Type: {type(is_learning)}")
print(f"Is Expert: {is_expert}")

# Collections
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_dict = {"name": "Python", "version": 3.9}
my_set = {1, 2, 3, 4, 5}

print("\n=== Collections ===")
print(f"List: {my_list}, Type: {type(my_list)}")
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")
print(f"Dictionary: {my_dict}, Type: {type(my_dict)}")
print(f"Set: {my_set}, Type: {type(my_set)}")

# Type Conversion
num_string = "123"
num_int = int(num_string)
num_float = float(num_string)

print("\n=== Type Conversion ===")
print(f"String to Int: {num_int}, Type: {type(num_int)}")
print(f"String to Float: {num_float}, Type: {type(num_float)}")
