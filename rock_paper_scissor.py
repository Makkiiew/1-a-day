import random

option = ["Rock", "Paper", "Scissors"]
player_input = input("Rock, Paper or Scissors: ").capitalize()
computer_input = random.choice(option)
print(f"Player Choice: {player_input}")
print(f"Computer Choice: {computer_input}")
if player_input == computer_input:
    print("Tie")
elif (player_input == "Rock" and computer_input == "Scissors") or \
     (player_input == "Paper" and computer_input == "Rock") or \
     (player_input == "Scissors" and computer_input == "Paper"):
    print("You Win")
else:
    print("Compter Wins")
