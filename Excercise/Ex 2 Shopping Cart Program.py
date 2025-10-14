# Shopping Cart Program

item = input("What is the item you like")
price = float(input("What is the price of the item"))
quantity = int(input("How many times do you like it?"))
total = price * quantity

print(f"You have Bought {item} and the Quantity is {quantity}")
print(f"The total is: {total}")