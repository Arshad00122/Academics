#Rock paper scissor
import random

possible_actions = ["rock", "paper", "scissors"]

def Ai_outcome(x):
    return random.choice(x)

while True:
    
    user_action=input("Enter (rock or paper or scissors):").lower()

    if user_action == Ai_outcome(possible_actions):
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if Ai_outcome(possible_actions) == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if Ai_outcome(possible_actions) == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if Ai_outcome(possible_actions) == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print ("i don't know that.")

