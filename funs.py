#from pokemons import *

def menu_combat():
    print("1. Atacar")
    print("2. Cambiar Pokemon")
    option_menu_combat = int(input("Opcion: "))-1
    return option_menu_combat

def combat(pokemon_atack, pokemon_defen):
    print("----------------")
    print(f"Ataca: {pokemon_atack.name}")
    print("Elige un ataque de tu pokemon:")
    for i, attack in enumerate(pokemon_atack.attacks):
        print(f"{i+1}. {attack}")
    user = int(input("Opcion: ")) - 1
    pokemon_defen.recive_damage(pokemon_atack.attacks[user])
    print("----------------")
    print(pokemon_defen)

def change_pokemon(pokemons_player):
    pokemon_change = print("En construccion cambiar de Pokemon")
    print("Tus pokemos:")
    [print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons_player)]
    return pokemon_change

def turno_pj(pokemons_player, pokemon_atack, pokemon_defen, cont_turnos, option_submenu_ok):
    print("----------------")
    print(f"TURNO:{cont_turnos} --- {pokemon_atack.name}")
    option_menu_combat = menu_combat()
    if option_menu_combat == 0:
        combat(pokemon_atack, pokemon_defen)
        option_submenu_ok = False
    elif option_menu_combat == 1:
        change_pokemon(pokemons_player)
        option_submenu_ok = False
    return option_submenu_ok

