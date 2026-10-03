class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def describe(self):
        """ ',' is the seperator in the .join method"""
        print(f"A {self.size} pizza with {', '.join(self.toppings)}.")

    @classmethod
    def luxury_margherita(cls, size):
        return cls(size, ["mozzarella", "fresh basil", "extra virgin olive oil"])
    
    @staticmethod
    def is_healthy(topping):
        healthy_stuff = ["mushrooms", "peppers", "basil", "onions"]
        return topping.lower() in healthy_stuff
    
pizza1 = Pizza("Small",["cheese", "pepperoni"])
pizza2 = Pizza("Large",["peppers","onions","mozzarella"])
pizza3 = Pizza.luxury_margherita("Medium")


print(Pizza.is_healthy("mushrooms"))

pizza1.describe()
pizza2.describe()
pizza3.describe()