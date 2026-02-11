# Ask the user for their age
try:
    age = int(input("Enter your age: "))

    # Check if age is negative
    if age < 0:
        print("⚠️ Age cannot be negative.")

    # If user is 18 or older
    elif age >= 18:
        print("✅ You are old enough to vote.")

    # If user is under 18
    else:
        years_left = 18 - age
        print(f"⏳ You have to wait {years_left} year(s) to vote.")

# Handle non-numeric input
except ValueError:
    print("❌ Please enter a valid number for age.")
