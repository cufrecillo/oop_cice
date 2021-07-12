from pokemons import *
from funs import *

print(" POKEMON ".center(50, "#"))
# print("Oak: Selecciona tu primer Pokemon...")
# [print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
# user_option = int(input("Opcion: "))-1
# pokemon_a = pokemons[user_option]

# print(pokemon_a)
# print("----------------")
# rest_pokemons = pokemons.copy()
# rest_pokemons.remove(pokemon_a)
# pokemon_b = random.choice(rest_pokemons)
# print("Te vas a enfrentar a...")
# print(pokemon_b)

pokemons_playerA = [charmander, squirtle, meganium]
pokemons_playerB = [bulbasaur, vulpix, golduck]

pokemon_a = random.choice(pokemons_playerA)
pokemon_b = random.choice(pokemons_playerB)
print(pokemon_a)
print("----------------")
print(pokemon_b)


cont_turnos = 0
pokemon_alive = True

while pokemon_alive:
    cont_turnos += 1

    option_submenu_ok = True
    while option_submenu_ok:
        option_submenu_ok = turno_pj(pokemons_playerA, pokemon_a, pokemon_b, cont_turnos, option_submenu_ok)
    if pokemon_b.is_alive == False:
        pokemon_alive = False
    else:
        option_submenu_ok = True
        while option_submenu_ok:
            option_submenu_ok = turno_pj(pokemons_playerB, pokemon_b, pokemon_a, cont_turnos, option_submenu_ok)
        if pokemon_a.is_alive == False:
            pokemon_alive = False



