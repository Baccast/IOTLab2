
while True:
    try:
        # Prompts the user with the 2 required values
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        break
    except ValueError:
        # Catches any wrong input and gives and error message and restarts
        print("Invalid input. Please enter a valid number.")

# Calculates the required numbers
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

# Display the results
print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Division: ", division)