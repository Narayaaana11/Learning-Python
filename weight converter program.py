# Ask the user to enter a weight
try:
    weight = float(input("Please enter a weight: "))
    units = input("Please enter a unit (L for pounds / K for kilograms): ").strip().upper()

    # Convert based on the unit entered
    if units == "L":  # Pounds to Kilograms
        converted_weight = weight / 2.205
        print(f"✅ Weight is {round(converted_weight, 2)} kg")

    elif units == "K":  # Kilograms to Pounds
        converted_weight = weight * 2.205
        print(f"✅ Weight is {round(converted_weight, 2)} lb")

    else:
        print("❌ Please enter a valid unit: 'L' or 'K'.")

except ValueError:
    print("⚠️ Invalid input. Please enter a numeric value for weight.")
