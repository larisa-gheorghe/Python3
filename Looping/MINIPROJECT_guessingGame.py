# from random import randint

# number = randint(1,11)
# guess = int(input("Guess a number between 1 and 10: "))
# more = "y"

# while more == "y":
#     while guess != number:
#         if guess < number:
#             print("Too low, try again!")
#         else:
#             print("Too high, try again!")
#         guess = int(input())

#     print("You guessed it! You won!")
#     print(number)

#     more = input("Do you want to keep playing? (y/n) ")

#     if more == "n":
#         break

#     number = randint(1,11)
#     guess = int(input("Guess a number between 1 and 10: "))
#     while guess != number:
#         if guess < number:
#             print("Too low, try again!")
#         else:
#             print("Too high, try again!")
#         guess = int(input())

from random import randint

number = randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("You guessed it! You won!")
        more = input("Do you want to keep playing? (y/n) ")
        if more =="y":
            number = randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")
            break

