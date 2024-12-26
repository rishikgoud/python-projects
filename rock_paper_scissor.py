import random
def rps_game():
    emojis = {'r':'🪨','p':'📃', 's':'✂️'}
    strings = ["r","p","s"]
    comp_choice = random.choice(strings)
    while True:
        user_choice = input("Rock, Paper or Scissor (r/p/s): ")
        if user_choice not in strings:
            print("Invalid Choice")
            continue

        print("Computer choose ", emojis[comp_choice])
        print("You choose ", emojis[user_choice])
        # print(comp_choice)
        if((user_choice == "p" and comp_choice == "s")or (user_choice == "s" and comp_choice == "r")or(user_choice == "r" and comp_choice == "p")):
            print("You lose")
        elif((user_choice == "s" and comp_choice == "p") or (user_choice == "p" and comp_choice == "r") or (user_choice == "r" and comp_choice == "s")):
            print("You Win")   
        else:
            print("The game is tie")

        continue_rps =  input("Continue? (y/n): ").lower()
        if(continue_rps != 'y'):
            print("Thanks for playing")
            break
rps_game()