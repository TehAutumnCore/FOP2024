# Define an exception named OutOfRangeError.
#   Write a function named name_the_number 
#       that asks the user for an integer, and 
#       if it's equal to 1, 
#           prints "one"; 
#       if it's equal to 2, 
#           prints "two", and 
#       if it's equal to 3, 
#           prints "three". 
#       
# If the the parameter is not one of those three values, the function should 
#           raise an OutOfRangeError. 
# Write code that calls 
#       name_the_number in a try block, 
# and handles the possible OutOfRangeError in an except block. 
#       It should handle an OutOfRangeError by printing "That's not one of the allowed values!"

""""
class OutOfRangeError(Exception):
    pass

int_asked_for = int(input("Enter an integer: "))

def name_the_number(int_asked_for):
    if int_asked_for == 1:
        print("one")
    elif int_asked_for == 2:
        print("two")
    elif int_asked_for == 3:
        print("three")
    else:
        raise OutOfRangeError

try: 
    name_the_number(int_asked_for)
except OutOfRangeError:
    print("That's not one of the allowed values!")
    """

class OutOfRangeError(Exception):
    pass

def name_the_number():
    try:
        int_asked_for = int(input("Enter an integer (1,2,3): "))
        if int_asked_for == 1:
            print("one")
        elif int_asked_for == 2:
            print("two")
        elif int_asked_for == 3:
            print("three")
        else:
            raise OutOfRangeError
    except OutOfRangeError:
        print("That's not one of the allowed values!")
    except ValueError:
        print("please enter a valid integer")

# try:
#     name_the_number()
# except ValueError:
#     print("Please enter a valid integer")