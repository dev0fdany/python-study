class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def speak(cls):
        print("some sound!")

class Dog(Animal):
    
    @classmethod
    def speak(cls):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, age , breed):
        super().__init__(name , age)
        self.breed = breed

    @classmethod
    def speak(cls):
        print("Meow!")


cat = Cat("Bili", 4, "Jangli")
dog = Dog("Kutah", 6)

Animal.speak()
cat.speak()
print(cat.breed)
dog.speak()

print(isinstance(cat, Cat))
print(isinstance(dog, Dog))

print(issubclass(Cat, Animal))
print(issubclass(Dog, Animal))
print(issubclass(Cat, Dog))
