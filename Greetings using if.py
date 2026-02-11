# Ask the user for their name
name = input("What is your name? ").strip()

# Ask the user for their age
# We use a try-except block to handle invalid number input
try:
    age = int(input("How old are you? "))

    # Check eligibility based on age
    if age >= 18:
        print(f"✅ Welcome to the club, {name}! You are eligible.")
    else:
        print(f"❌ Sorry {name}, you are not eligible because you are only {age} years old.")

# Handle the case where the user does not enter a valid number
except ValueError:
    print("⚠️ Please enter a valid number for your age.")
