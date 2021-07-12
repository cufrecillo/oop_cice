from pokemons import *

def combat(pokemon_atack, pokemon_defen, cont_turnos):
    print("----------------")
    print(f"Turno :{cont_turnos}")
    print(f"Ataca: {pokemon_atack.name}")
    print("Elige un ataque de tu pokemon:")
    for i, attack in enumerate(pokemon_atack.attacks):
        print(f"{i+1}. {attack}")
    user = int(input("Opcion: "))
    pokemon_defen.recive_damage(pokemon_atack.attacks[user -1])
    print("----------------")
    print(pokemon_defen)