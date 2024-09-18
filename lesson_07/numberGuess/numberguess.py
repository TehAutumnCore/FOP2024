# Write a program that prompts the user for an integer that the player will try to guess. If the player's guess is higher than the target integer, the program should display "too high".
# If the user's guess is lower than the target integer, the program should display "too low". The program should use a loop that repeats until the user correctly guesses the integer. 
# Then the program should print how many guesses it took.  When you run your program it should match the following format:

# Enter the integer for the player to guess.
# -12
# Enter your guess.
# 100
# Too high - try again:
# 50
# Too high - try again:
# -2000
# Too low - try again:
# -12
# You guessed it in 4 tries.

# # If the user guesses the integer in 1 try, then your program should print "You guessed it in 1 try."

import random 
goal = random.randint(-50,50)
number_of_guesses = 0
guess = None

while guess != goal:
    guess = int(input("enter your guess!: "))
    number_of_guesses+=1 

    if guess > goal:
        print("Too high, Try again!: ")
    elif guess < goal:
        print("Too low, Try again!: ")
    
if number_of_guesses == 1:
    print(f"The number was {guess}. You guessed it in 1 try!")
else:
    print(f"You guessed correctly! The number was {guess}. You guessed it in {number_of_guesses} tries.")


#


# won = False
# tries = 1

# while won == False:
#     playerGuess = int(input("Enter your guess: "))
#     if playerGuess == correctNumber:
#         if tries > 1:
#             print(f"You guessed it in {tries}")
#         else:
#             print(f"You guessed it in 1 try")
#         won = True
#     elif playerGuess > correctNumber:
#         tries +=1
#         print("Too high, try again")
#     elif playerGuess < correctNumber:
#         tries +=1
#         print("Too low, try again")