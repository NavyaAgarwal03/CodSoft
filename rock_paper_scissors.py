import random

choices = ("rock", "paper", "scissors")
invalid = True

while invalid:

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Enter a choice (rock, paper, scissors): ")

    print("Player: {player}")
    print("Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        invalid= False

print("Thanks for playing!")

         

