response = input("Would you like to food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("Have no food!")

name = input("What is your name? ")
if name == "":
    print("You did not enter a name")
else:
    print(f"Hello {name}")

for_sale = True

if for_sale:
    print("Item is for sale")
else:
    print("Item is not for sale")

online = True
if online:
    print("Online")
else:
    print("Offline")
