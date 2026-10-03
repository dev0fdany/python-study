class Account:
    bank_name = "AYC Bank"
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        print('{} deposited {}$'.format(self.owner, amount))

    def withdraw(self, amount: int):
        if self.balance - amount < 0:
            print('@{} cannot withdraw {}$'.format(self.owner, amount))
            print("Insufficient funds")
            print("Your balance is: {}$".format(self.balance))
        else:
            self.balance -= amount
            print('{} took {}$'.format(self.owner, amount))
    
    def description(self):
        return "{}: {} currently has {}$".format(self.bank_name, self.owner, self.balance)

account1 = Account("James", 400)
account2 = Account("Carlo", 500)
account1.bank_name = "ABC bank"
account1.deposit(300)
account2.deposit(400)

print(account1.description())
print(account2.description())
