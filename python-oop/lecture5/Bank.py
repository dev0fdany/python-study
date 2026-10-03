class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return 'BankAccount({}, {})'.format(self.owner, self.balance)
    def __str__(self):
        return '{} {}$'.format(self.owner, self.balance)
    def __len__(self):
        return len(self.owner)
    def __add__(self, other):
        return self.balance + other.balance

acc1 = BankAccount("Ali", 1500)
acc2 = BankAccount("Sara", 2800)

print(acc1)
print(repr(acc1))
print(f"{len(acc1)} Characters.")
print(f"{acc1 + acc2}$")