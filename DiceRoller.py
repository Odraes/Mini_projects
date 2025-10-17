import random

dice_tracker = 0
while True:
    print("roll the dice? (Y/N)")
    answer = input().strip().upper()


    if answer == "Y":
        try:
            dice_number = int(input("How many dice would you like to roll? "))
            if dice_number <= 0:
                print("Please enter a positive number.\n")
                continue
        except ValueError:
            print("Invalid number. Please enter an integer.\n")
            continue

        for i in range(dice_number):
            die1 = random.randint(1, 9)
            die2 = random.randint(1, 9)
            print(f"the dice is ({die1}) ({die2})")
            dice_tracker += 1
        print(f'Total dice rolled so far: {dice_tracker}')


    elif answer == "N":
        print("thank you for playing, You rolled the dice {dice_tracker} time(s).")
        break
    else:
        print("invalid choice, Please type 'Y' or 'N'.\n")

