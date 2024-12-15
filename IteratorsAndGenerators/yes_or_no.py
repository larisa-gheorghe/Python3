def yes_or_no():
    value = "yes"
    while True:
        if value == "yes":
            yield value
            value = "no"
        else:
            yield value
            value = "yes"


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'