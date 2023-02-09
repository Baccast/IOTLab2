while True:
    try:
        # Asks for a float input
        celsius = float(input("Enter the temperature in Celsius: "))
        break
    except ValueError:
        # Prompts error message if input is not float and loop will restart
        print("Wrong input Please try again: ")

# Calculates temperature in fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Prints output
print("%.1f ˚C is equal to %.1f ˚F." % (celsius, fahrenheit))
        