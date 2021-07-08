elements = ["fire", "grass", "water"]

def create_pokemon(name, element, HP):
    pokemon = {
        "name": name,
        "element": element,
        "HP": HP,
        "attacks": attacks
    }
    return pokemon

def create_attack(name, element, damage):
    attack = {
        "name": name,
        "element": element:
        "damage": damage
    }
    return attack

def learn(pokemon, attack):
    pokemon["attacks"].append(attack)

