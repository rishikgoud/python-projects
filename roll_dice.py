import random
def dice_roll():
    a = input("Roll the dice(Y/N): ")
    if(a.lower()=="n"):
        print("Thanks for Playing.")
    elif(a.lower()=="y"):
        b=random.randint(1,6)
        c = random.randint(1,6)
        print(f'({b}, {c})')
        dice_roll()
    else:
        print("Invalid choice")
        dice_roll()

dice_roll()