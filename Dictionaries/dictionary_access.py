from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if bakery_stock.get(food):
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")