#Exception handling

# numerator = 10 ** 3
# denominator = int(input("ente ra number for the denominator: "))

# try:
#     result = float(numerator/denominator)
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero is undefined")

class ImaginearyNumberError(Exception):
    pass

user_input = int(input("Enter a positive Integer: "))

if user_input >= 0:
    finalResult = user_input ** 0.5
else:
    raise ImaginearyNumberError()