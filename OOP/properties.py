class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age
    #
    # def set_age(self, new_age):
    #     if new_age >=0:
    #         self._age = new_age
    #     else:
    #         self.age = 0

    # getter
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self.age = 0

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

jane = Human("Jane", "Goodall", 50)
print(jane.age)
jane.age = -100
print(jane.age)
print(jane.full_name)