import random


def dice():
    while True:
        user = input("Do you want to roll the dice? (Y/N): ")

        # The User Decides = Y (yes)
        if user.lower() in {'yes', 'y'}:
            dice_number = input("How many? (1/2): ")
            if dice_number.lower() in ['1', 'one']:
                num = random.randrange(1, 6)
                print(f"Dice rolled! You've got: {num}")
            elif dice_number in ['2', 'two']:
                num = random.randrange(1, 6)
                num2 = random.randrange(1, 6)
                print(f"Dices rolled! You've got: {num} and {num2}")
                print(f"That will be: {num+num2}")
            else:
                print("Invalid prompt. Try again.\n")
        # The User Decides = N (no)
        elif user == 'n':
            print("See you next time!")
            continue
        # Invalid prompt
        else:
            print("Invalid answer, try again:\n ")


dice()
