import random

while true:
    print("roll the dice? (Y/N)")
    answer = input()
    answer = answer.upper()
    if answer == "Y":
        die1 = random.randint(1, 9)
        die2 = random.randint(1, 9)
        print(f"the dice is ({die1}) ({die2})")
    elif answer == "N":
        print("thank you for playing")
        break
    else:
        print("invalid choice")

