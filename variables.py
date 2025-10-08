# This is my first python program
print('I like Vada')
print("It's really good")

#sring
first_name='Narayana'
last_name='Thota'
print(f"my name is {first_name} {last_name}")

#integer
age = 25
std_count = 36
print(f'my age is {age}')
print(f'my standard count is {std_count}')

#float
price=10.50
gpa=7.89
distance = 110

print(f'price of a water bottle is {price} \nmy gpa is {gpa} \nmy home town distance from college is {distance}')

#boolean

is_student = True
for_sale = False

if is_student:
    print('I am a student.')
else:
    print('I am a teacher.')

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0w

x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 'awesome'
def my_func():
    x = 'fantastic'
    print('Python is '+x)
my_func()
print('Python is '+x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


