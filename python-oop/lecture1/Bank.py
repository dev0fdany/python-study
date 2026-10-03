class Account:
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
        return "{} currently has {}$".format(self.owner, self.balance)

account1 = Account("James", 400)
account2 = Account("Carlo", 500)

account1.deposit(300)
account2.deposit(400)

account1.withdraw(200)
account2.withdraw(1000)

account1.description()
account2.description()