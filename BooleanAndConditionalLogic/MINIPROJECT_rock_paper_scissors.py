from random import randint

print("...rock...\n...paper...\n...scissors...")

player1 = input("(enter Player 1's choise): ").lower()
player2 = None

rand_num = randint(0,2)

if rand_num == 0:
    player2 = "rock"
elif rand_num == 1:
    player2 = "paper"
else:
    player2 = "scissors"

print(f"Player 2's choise == {player2}")
print("SHOOT!")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins")
    else:
        print("player2 wins")
elif player1 == "paper":
    if player2 == "scissors":
        print("player2 wins")
    else:
        print("player1 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    else:
        print("player1 wins")
else:
    print("Something went wrong")