import random
#A rock paper scissor game using python radom module, if statments and while loop
running = True
options = ("rock", "paper", "scissors")
while running:
    player = input("Enter an options (Rock, Paper, Scissors): ").lower()
    computer = random.choice(options)

    while player not in options:
        player = input("Not among the options (Rock, Paper, Scissors): ").lower()
    print(f"The computer chose: {computer}")
    print(f"The player chose: {player}")
    if player == computer:
        print("It's a tie")

    elif player == "sisccors" and computer == "paper":
        print("You won!!!")

    elif player == "rock" and computer == "scissors":
        print("You won!!!")

    elif player == "paper" and computer == "rock":
        print("You won!!!")

    else:
        print("You lost")

    paly_again = input("Play again (y/n)").lower()
    if paly_again != "y":
        running = False