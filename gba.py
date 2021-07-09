from pokemons import *

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
