# Fence Cost Calculator
# it will be in meters

# Rescyling the number checker function from area-and-perim-calc.py
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



# main routine starts here

keep_going = ""
while keep_going == "":

    #get width and height
    width = num_check("Enter the width: ")
    height = num_check("Enter the height: ")
    cost = num_check("Enter the cost of the fence per meter: ")

    # calculate perimeter and cost for the fence based of user input
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # display output for the user
    print()
    print(f"perimeter: {perimeter} meters")
    print (f"price: the cost of the fence is ${price:.2f}")

    # continue message for the user
    keep_going = input("again? enter to keep going or type n to quit: ")

    # goodbye message for the user
    if keep_going == "n":
        print("Thank you for using the calculator​")
    

