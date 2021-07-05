# ROCK PAPER SCISSORS GAME

# Remember the rules:

# rock beats scissors
# scissors beats paper
# paper beats rock

import getpass

print("""Let's play a game of rock paper scissors!! 
You'll need a partner to play this game.
To End the Game input any response other than rock, paper or scissors.""")
print("-" * 100)

play_again = "y"

u1_score = 0

u2_score = 0

while play_again == "y":

    user_1 = getpass.getpass(
        prompt="Player 1, enter your choice from Rock, Paper or Scissors ").lower()

    user_2 = getpass.getpass(
        prompt="Player 2, enter your choice from Rock, Paper or Scissors ").lower()

    print("Player 1 typed", user_1.capitalize())

    print("Player 2 typed", user_2.capitalize())

    if user_1 == user_2:
        print("Game tied!!")

    elif user_1 == "rock" and user_2 == "scissors":
        print("Player 1 wins!!")
        u1_score += 1

    elif user_1 == "paper" and user_2 == "rock":
        print("Player 1 wins!!")
        u1_score += 1

    elif user_1 == "scissors" and user_2 == "paper":
        print("Player 1 wins!!")
        u1_score += 1

    elif user_1 == "scissors" and user_2 == "rock":
        print("Player 2 wins!!")
        u2_score += 1

    elif user_1 == "rock" and user_2 == "paper":
        print("Player 2 wins!!")
        u2_score += 1

    elif user_1 == "paper" and user_2 == "scissors":
        print("Player 2 wins!!")
        u2_score += 1

    else:
        print("Somebody typed something incorrect")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "n":
            break

print("Game Over")

print("The final score is Player 1: ", u1_score, "| Player 2:", u2_score)
