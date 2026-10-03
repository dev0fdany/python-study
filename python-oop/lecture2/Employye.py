class Employye:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def apply_raise(self):
        self.pay = int(self.pay * Employye.raise_amount)
        print("{}'s salary has been raised.".format(self.last))
    def description(self):
        return '{} {}, {}$'.format(self.first, self.last, self.pay)

emp1 = Employye("Seishiro","Nagi",118500)
emp2 = Employye("Ryosuke","Kira", 105000)

print(Employye.raise_amount)
print(emp1.last, emp1.pay)
print(emp1.last, emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.description())
print(emp2.description())
Employye.raise_amount = 1.10
print(Employye.raise_amount)
print(emp1.last, emp1.pay)
print(emp1.last, emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.description())
print(emp2.description())