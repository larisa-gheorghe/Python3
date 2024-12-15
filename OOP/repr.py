class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name


dude = Human()
print(dude)  # 'somebody'
colt = Human(name="Colt Steele")
print(colt)
