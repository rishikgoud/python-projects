import random
guess_no = random.randint(1,100)
while True:
    input_user = int(input("Guess the number between 1 and 100: "))
    if(input_user > guess_no):
        print("Too high")
    elif(input_user< guess_no):
        print("Too low")
    elif(input_user == guess_no):
        print("Congratulation! You guessed the number")
        break
    else:
        print("Please enter a valid number")
