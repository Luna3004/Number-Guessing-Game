import os
import generate_random_number

import random

os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Number Guessing Game! You will be able to assign a lower/upper bound into the random generator machine. The machine will pick a number and you will have to guess it in under 10 trys. Good luck!")
print("-----------------------------------------------------------------")

lower_bound = int(input("What is the lower bound of the range? "))
upper_bound = int(input(" What is the upper bound of the range? "))

number = generate_random_number(lower_bound, upper_bound)
print(number)

guess = int(input("What number do you guess? "))

i = 1
while i < 10:
    if guess != number:
        if guess >= upper_bound : 
            if guess < lower_bound or guess > upper_bound:
                print("That is outside the range you assigned. Again!")
                i = i + 1
                guess = int(input("What number do you guess? "))
            else:
                print("Please try again. Your guess is too high!")
                guess = int(input("What number do you guess? "))
                i = i + 1
        elif guess <= number: 
            if guess < lower_bound or guess > upper_bound:
                print("That is outside the range you assigned. Again!")
                i = i + 1
                guess = int(input("What number do you guess? "))
            else:
                print("Please try again! Your guess is too low!")
                guess = int(input("What number do you guess? "))
                i = i + 1
    else: 
        print("Congratulations! You got it right")
        print(f"Number of Guesses: {i}")
        break
else: 
  print(f"Better Lucky Next Time!The number was {number}")
  print(f"Number of Guesses: {i}")
