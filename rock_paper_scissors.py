import random

print("******* Welcome to Python Rock, Paper, Scissors! *******")

playing = input("Would you like to play? ").lower()

if playing != "yes" and playing != "y": 
    print("Maybe Next Time!")
    quit() 

user_wins = 0
ai_wins = 0


choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit. ").lower()
    if user_input in ["q", "quit"]:
        break
    if user_input not in choices:
        continue #will keep asking them until they put in a valid response

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1. scissors: 2
    ai_pick = choices[random_number]
    print("Computer chose", ai_pick + ".")

# User Input Conditions
    if user_input == "rock" and ai_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and ai_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and ai_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == ai_pick:
        print("Its a tie! Try again...")
    else:
        print("You Lose :(")
        ai_wins += 1

print("You won", user_wins, "times.")
print("The computer won", ai_wins, "times.")
print("See you next time!")
