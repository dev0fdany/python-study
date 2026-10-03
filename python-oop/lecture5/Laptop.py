class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def __repr__(self):
        return 'Laptop({}, {}, {})'.format(self.brand, self.model, self.price)

    def __str__(self):
        return '{} {} {}$'.format(self.brand, self.model, self.price)
    
    def __add__(self, other):
        return '{}$'.format(self.price+other.price)
    def __len__(self):
        return len(self.model)
    
lap1 = Laptop("Dell", "XPS13", 1200)
lap2 = Laptop("HP", "EliteBook", 900)

print(lap1)
print(repr(lap1))
print(len(lap1))
print(lap1 + lap2)