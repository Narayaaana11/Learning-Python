# Ask the user to enter an operator
operator = input("Please enter an operator (+ - / * %): ").strip()

# Use try-except to prevent program crash from invalid number input
try:
    # Ask the user for two numbers
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))

    print(f"\nWe are performing '{operator}' operation")

    # Perform calculation based on operator
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        # Check for division by zero
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed.")
            exit()
        result = num1 / num2

    elif operator == "%":
        # Check for modulo by zero
        if num2 == 0:
            print("❌ Error: Modulo by zero is not allowed.")
            exit()
        result = num1 % num2

    else:
        print("❌ Please enter a valid operator.")
        exit()

    # Display rounded result (2 decimal places for better precision)
    print(f"✅ Result: {round(result, 2)}")

except ValueError:
    print("⚠️ Invalid input. Please enter numeric values only.")
