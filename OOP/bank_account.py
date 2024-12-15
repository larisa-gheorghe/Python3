class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, sum):
        self.balance += sum
        return self.balance

    def withdraw(self, sum):
        self.balance -= sum
        return self.balance