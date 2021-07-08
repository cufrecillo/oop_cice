import random

elements = ["fire", "grass", "water"]

class Pokemon:
    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []

    def __str__(self):
        return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"

    def learn(self, attack):
        return self.attacks.append(attack)

    def recive_damage(self, attack):
        damage = random.randint(0, attack.damage)
        self.HP -= damage

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: {self.damage}"


charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)

flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor_leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 35)

charmander.learn(flamethrower)
charmander.learn(razor_leaf)
bulbasaur.learn(razor_leaf)
print(charmander)
print("----------------")
print(bulbasaur)
print("----------------")

for i, attack in enumerate(charmander.attacks):
    print(f"{i+1}. {attack}")

user = int(input("Opcion: "))
bulbasaur.recive_damage(charmander.attacks[user -1])
print(bulbasaur)


