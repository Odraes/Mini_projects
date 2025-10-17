import random

dice_tracker = 0
while True:
    print("roll the dice? (Y/N)")
    answer = input()
    answer = answer.upper()

    if answer == "Y":
        print("how many dice?")
        diceNumber = input()
        diceNumber = int(diceNumber)
        for i in range(diceNumber):
            die1 = random.randint(1, 9)
            die2 = random.randint(1, 9)
            print(f"the dice is ({die1}) ({die2})")
            dice_tracker += 1
        print(f'how many time you have roll the die: {dice_tracker}')


    elif answer == "N":
        print("thank you for playing")
        break
    else:
        print("invalid choice")

