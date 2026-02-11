# Ask the user if they would like food
response = input("Would you like food? (Y/N): ").strip().lower()

# Check the user's response
if response == "y":
    print("✅ You can have food.")
elif response == "n":
    print("❌ You cannot have food.")
else:
    print("⚠️ Please enter 'Y' for Yes or 'N' for No.")
