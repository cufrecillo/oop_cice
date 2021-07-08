from pokemons import *

# POKEMONS
charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)

# ATTACKS
flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor_leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 35)

charmander.learn(flamethrower)
charmander.learn(razor_leaf)
bulbasaur.learn(razor_leaf)
squirtle.learn(surf)
print(charmander)
print("----------------")
print(bulbasaur)
print("----------------")
print(squirtle)
print("----------------")

for i, attack in enumerate(charmander.attacks):
    print(f"{i+1}. {attack}")
user = int(input("Opcion: "))
print("----------------")

bulbasaur.recive_damage(charmander.attacks[user -1])
print(bulbasaur)
