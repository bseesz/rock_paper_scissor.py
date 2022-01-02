#create a game of rock, paper, scissors


#import random module for player 2
import random
action = ["rock", "paper", "scissors"]

#create while loop so game continues for as long as the player want
while True:

#welcome message
    print("Welcome to Rock, Paper, Scissors: the game where you get cut, crushed or shawdowed to defeat by your opponent!")

#retrieve player 1 input
    player1 = input("What would you like to throw down? Rock, paper, or scissors?: ").lower().strip()

#create a player 2 with a random choice from the computer
    player2 = random.choice(action)
    print(f"Player 2 shoots: {player2}!")

    print(f"You chose {player1}, player 2 chose {player2}.")

#create conditional statements to announce results
    if player1 == player2:
        print(f"Both players selected {player2}. It's a tie!")
    if player1 == "rock" and player2 == "paper":
        print("Paper smothers rock. Player 2 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Paper smothers rock. Player 2 wins!")
    elif player1 =="paper" and player2 == "scissors":
        print("Scissors cut paper. Player 2 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Scissors cut paper. Player 1 wins!")
    elif player1 == "rock" and player2 =="scissors":
        print("Rock smashes scissors. Player 1 wins!")
    elif player1 =="scissors" and player2 == "rock":
        print("Rock smashes scissors. Player 1 wins!")
else:
    print("That's not an option, my friend! You lose!")

