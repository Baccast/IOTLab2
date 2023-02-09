while True:
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        break
    except ValueError:
        print("Wrong input Please try again: ")
        
fahrenheit = (celsius * 9 / 5) + 32

print("%.1f ˚C is equal to %.1f ˚F." % (celsius, fahrenheit))
        