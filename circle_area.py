while True:
    # Tries to recieve a float input from the user
    try:
        radius = float(input("Enter the radius of the circle in cm: "))
        break
    except ValueError:
        # If the input is wrong it prints out the error message and starts over
        print("Wrong input Please try again: ")

# Calculates the area of the circle using the pi * radius squared
area = 3.14 * radius * radius;

# Prints ou the given 
print("The area of a circle with the radius %.2f cm is %.2f cm2" % (radius, area))        