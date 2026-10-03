from random import choice
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    attacks = ["crack", "thud", "whack", "smack", "bam", "snap"]
    def attack(self):
        print(f"{choice(self.attacks)}!")

    def show_health(self):
        print(f"HEALTH: {self.health} ")

class  Warrior(Character):
    attacks = ["Sssssst", "shhhnnkt", "Zwee", "whick", "shink", "Ting"]
class Mage(Character):
    attacks = ["Fwooomph", "Krak-thoom", "Shhh-tink", "Krrr-chk", "Bzzzz-vromm", "Thwip-thwip-thwip"]

class Archer(Character):
    attacks = ["Sssss-t", "Twang", "Thwack", "Pluck", "ssss-vwoot", "Thwup"]


the_archer = Archer("The Flash", 100)
the_mage = Mage("The Brinbed Caps", 200)
the_warrior = Warrior("Sword Saint", 500)

the_warrior.attack()
the_mage.attack()
the_archer.attack()