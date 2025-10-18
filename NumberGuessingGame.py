import random

random_number = random.randint(1, 100)
while True:
    try:
        answer = int(input("Guess the number between 1 and 100? "))
    except ValueError:
        print("Invalid number. Please enter an integer.\n")
        continue
    if answer < random_number:
        print("The number was too low")
        continue
    elif answer > random_number:
        print("The number was too high")
        continue
    else:
        print("You Guess the number!")
        break