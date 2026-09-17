
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than zero next time")
        quit()
else:
    print("Please type a positive number next time")
    quit()

random_number = random.randint(1, top_of_range)
print(random_number)
while True:
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("You were below the number!")
    else:
        print("You were above the number!")