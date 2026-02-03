# Exercise 2 Shopping Cart Program

item = input("What item you would like to buy")
price = float(input("What is the price of the item"))
quantity = int(input("How many items would you like?"))
total_price = price * quantity

print(f"You bought {item} in {quantity} items")
print("The total price is", total_price)