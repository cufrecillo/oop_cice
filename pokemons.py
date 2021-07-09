# https://github.com/vgenov-py/T-522/blob/master/pokemon.md

import random

elements = ["fire", "grass", "water"]
# fire > grass
# grass > water
# water > fire
# if > 1.5 // if < 0.5
#     fire grass water
# Fire    1   1.5   0.5
# GRass  0.5   1    1.5
# water  1.5   0.5   1

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
        print(damage)
        print(attack.element)
        print(self.element)
        if self.element == attack.element:
            self.HP -= damage
        else:
            if attack.element == "fire":
                if self.element == "grass":
                    self.HP -= damage * 1.5
                elif self.element == "water":
                    self.HP -= damage * 0.5
            elif attack.element == "grass":
                if self.element == "water":
                    self.HP -= damage * 1.5
                elif self.element == "fire":
                    self.HP -= damage * 0.5
            elif attack.element == "water":
                if self.element == "fire":
                    self.HP -= damage * 1.5
                elif self.element == "grass":
                    self.HP -= damage * 0.5

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: {self.damage}"


# POKEMONS
charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)

# ATTACKS
flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor_leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 35)

