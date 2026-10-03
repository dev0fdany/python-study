class Car:
    wheels = 4
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def description(self):
        return '{} {} has {} wheels.'.format(self.brand, self.model, self.wheels)

car1 = Car("Toyota", "Camry", "Silver") 
car2 = Car("BMW", "X5", "Black")
car3 = Car("Honda", "Civic", "Blue")
car3.wheels = 3

print(car1.description())
print(car2.description())
print(car3.description())


