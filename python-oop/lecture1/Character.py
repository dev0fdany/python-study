class Character:
    def __init__(self, name: str, health: int, level: int):
       self.name = name 
       self.health = health
       self.level = level
    
    def description(self):
        return "{} is level {} and has {} health.".format(self.name,self.level,self.health)

aot = Character("Levi", 100, 97 )
cg  = Character("Lelouch", 100, 98)
dnote = Character("L", 100, 99)

print(aot.description())
print(cg.description())
print(dnote.description())