from pokemons import *

print(" POKEMON ".center(50, "#"))

print("Oak: Selecciona tu primer Pokemon...")
[print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
user_option = int(input("Opcion: "))-1
pokemon_a = pokemons[user_option]

print(pokemon_a)
print("----------------")
rest_pokemons = pokemons.copy()
rest_pokemons.remove(pokemon_a)
pokemon_b = random.choice(rest_pokemons)
print("Te vas a enfrentar a...")
print(pokemon_b)
print("----------------")

cont_turnos = 0
pokemon_alive = True

while pokemon_alive:
    cont_turnos += 1
    print("Elige un ataque de tu pokemon:")
    for i, attack in enumerate(pokemon_a.attacks):
        print(f"{i+1}. {attack}")
    user = int(input("Opcion: "))
    pokemon_b.recive_damage(pokemon_a.attacks[user -1])
    print("----------------")
    print(f"Turno :{cont_turnos}")
    print(pokemon_b)
    if pokemon_b.is_alive == False:
        pokemon_alive = False
