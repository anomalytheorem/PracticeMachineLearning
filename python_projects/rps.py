import random

userw = 0
comw = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer = options[random_number]
    print("Computer picked", computer + ".")

    if user_input == "rock" and computer == "scissors":
        print("You won")
        userw += 1

    elif user_input == "paper" and computer == "rock":
        print("You won")
        userw += 1

    elif user_input == "scissors" and computer == "paper":
        print("You won")
        userw += 1

    elif user_input == computer:
        print("Tie")

    else:
        print("You lost fuckface.")
        comw += 1

print("Your score is",userw)
print("The computer's score is",comw)
print("Get fucked")
