# for num in range(1, 11):
#     print("\U0001f600" * num)

emoji = 1
space = 20
while emoji < 22:
    print(f".{" " * space}{"\U0001f600" * emoji}{" " * space}.")
    space -= 1
    emoji += 1