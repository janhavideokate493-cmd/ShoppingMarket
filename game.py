import random

player = input("Choose rock, paper, or scissor: ").lower()

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)

print("Computer chose:", computer)

if player == "rock" and computer == "scissor":
    print("Player won")

elif player == "scissor" and computer == "paper":
    print("Player won")

elif player == "paper" and computer == "rock":
    print("Player won")

elif player == computer:
    print("Tie")

elif player in choices:
    print("Computer won")

else:
    print("Invalid input")