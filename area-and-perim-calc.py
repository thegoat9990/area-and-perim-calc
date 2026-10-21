# Ask the user for the width and height
# (Assume they put in valid data)
'''width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

# Calculate the area and perimeter
area = width * height
perimeter = 2 * (width + height)

# Display the results
print(f"The area is: {area}")
print(f"The perimeter is: {perimeter}")'''

# Ask user for width and loop until they give a valid number above 0
def num_check(question):
    while True:
        try:
            value = float(input(question))
            if value > 0:
                return value
            else:
                print("Please enter a number more than 0.")
        except ValueError:
            print("Please enter a valid number.")

#main routine

keep_going = ""
while keep_going == "":
    width = num_check("Enter the width: ")
    height = num_check("Enter the height: ")

    # Calculate the area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display the results
    print(f"The area is: {area}")
    print(f"The perimeter is: {perimeter}")

    keep_going = input("Press enter to keep going or any key to quit ")
