import random
finish = False
while not finish:
    print("roll the dice? (Y/N)")
    answer = input()
    answer = answer.upper()
    if answer == "Y":
        dice = random.randint(1, 9)
        dice2 = random.randint(1, 9)
        print(f"the dice is ({dice}) ({dice2})")
        pass
    elif answer == "N":
        print("thank you for playing")
        finish = True
    else:
        print("invalid choice")

