class Dog:
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age

    def description(self):
        return "{} a {}, age is {}.".format(self.name, self.breed, self.age)
    
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Poodle", 5)

print(dog1.description())
print(dog2.description())