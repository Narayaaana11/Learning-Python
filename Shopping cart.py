# Exercise 2: Shopping Cart Program

# Taking input from the user
item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many items would you like? "))

# Calculating total price
total_price = price * quantity

# Displaying the result
print(f"You bought {quantity} {item}(s).")
print(f"The total price is: {total_price}")
