# # Initialize Variables
# Quarter = 25 #quarter
# Dime = 10 #dimes
# Nickel = 5  #nickels
# Penny = 1  #pennies

# #99 cents -> Q: 3, D: 2, N:0, P:4
# #40 cents -> Q: 1, D: 1, N: 4
# amount = int(input("Enter a number of cents: ")) 
# # amount = 40

# #Take the amount entered divide by quarters and round down
# Q = amount // Quarter
# remaining_after_quarters = amount % Quarter

# #Take the leftover and divide by dimes and round down
# D = remaining_after_quarters // Dime
# remaining_after_dimes = remaining_after_quarters % Dime

# #Take the leftover and divide by nickels and round down
# N = remaining_after_dimes // Nickel
# remaining_after_nickels = remaining_after_dimes % Nickel

# #Take the leftover and divide by pennys and round down
# P = remaining_after_nickels // Penny

# print("Your change will be: ")
# print(f"Q:{Q}")
# print(f"D:{D}")
# print(f"N:{N}")
# print(f"P:{P}")




cents = int(input("Please enter an amount in cents less than a dollar: "))

if 0 <= cents <= 99:
    quarters = cents //25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    pennies = cents % 5
    
    print(f"Your change will be Q: {quarters}, D: {dimes},N: {nickels}, P: {pennies}")
else:
    print("This is not a valid amount")