class Phone:
    company = "Samsung"
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def description(self):
        return "{} {}, Price: {}$".format(self.company,self.model,self.price)


phone1 = Phone("iPhone 16", 799)
phone2 = Phone("Galaxy S25", 799)
phone3 = Phone("Pixel 9", 799)

phone1.company = "Apple"
phone3.company = "Google"

print(phone1.description())
print(phone2.description())
print(phone3.description())


print(Phone.company)

print(phone1.__dict__)
print(phone2.__dict__)
print(phone3.__dict__)