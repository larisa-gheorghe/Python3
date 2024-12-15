from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player_score = 0
computer_score = 0
winning_score = 3

while player_score < winning_score and computer_score < winning_score:

    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        print("GAME ABORT")
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}" )

    if player == computer:
        print("It's a tie!")
        print(f"Player Score = {player_score}")
        print(f"Computer Score = {computer_score}")
    elif player == "rock":
        if computer == "scissors":
            player_score += 1
            print(f"Player wins this round!")
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Player Score = {player_score}")
        print(f"Computer Score = {computer_score}")
    elif player == "paper":
        if computer == "rock":
            print("Player wins this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Player Score = {player_score}")
        print(f"Computer Score = {computer_score}")
    elif player == "scissors":
        if computer == "paper":
            print("Player wins this round!")
            player_score += 1
        else:
            print("Computer wins this round!")	
            computer_score += 1
        print(f"Player Score = {player_score}")
        print(f"Computer Score = {computer_score}")
    else:
        print("Please enter a valid move!")
if player_score > computer_score:
    print("GAME WON BY PLAYER!!!!!!!!!!!!")
elif player_score == computer_score:
    print("It's a tie...")
else:
    print("GAME WON BY COMPUTER!!!!!!!!!!!!")
    