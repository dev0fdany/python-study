class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance
    
w1 = Wallet(250)
w2 = Wallet(400)
print(w1+w2)