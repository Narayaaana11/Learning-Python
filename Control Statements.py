age = float(input("Age: "))
if age >= 18:
    print("You are eligible")
elif age < 0:
    print("You are haven't born yet")
elif age > 25:
    print("You are too old to signup")
else:
    print("Not eligible")
