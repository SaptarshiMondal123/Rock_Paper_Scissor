import random
choices=["rock","paper","scissor"]
while True:
    
    player=None
    computer=random.choice(choices)
    
    while player not in choices:
        player=input("rock paper or scissor : ?").lower()
    if player==computer:
        print("Computer : ",computer)
        print("Player : ",player)
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print("Computer : ",computer)
            print("Player : ",player)
            print("You Looser! Try for the next time")
        if computer=="scissor":
            print("Computer : ",computer)
            print("Player : ",player)
            print("Bravo! You won")
    elif player=="paper":
        if computer=="scissor":
            print("Computer : ",computer)
            print("Player : ",player)
            print("You Looser! Try for the next time")
        if computer=="rock":
            print("Computer : ",computer)
            print("Player : ",player)
            print("Bravo! You won")
    elif player=="scissor":
        if computer=="rock":
            print("Computer : ",computer)
            print("Player : ",player)
            print("You Looser! Try for the next time")
        if computer=="paper":
            print("Computer : ",computer)
            print("Player : ",player)
            print("Bravo! You won")
    play_again=input("Play again? : (yes/no)").lower()
    if play_again != "yes":
        break
print("Bye Looser! Looks like you don't have the potential to win this game")