import requests

print("Welcome to your personal Pokedex.")
pokemon = (input("which Pokemon would you like to look up? ")).lower()

base_url = "https://pokeapi.co/api/v2/pokemon/"


while pokemon: 
    req = requests.get(base_url + pokemon) 
    if req.status_code == 200:  
        pokemon_data = req.json()
        pokemon_abilities = pokemon_data['abilities']
        pokemon_moves = pokemon_data['moves']
        pokemon_types = pokemon_data['types']
        print(f"{pokemon} has the following abilities: ")
        for ability in pokemon_abilities:
            print(f" {ability['ability']['name']}")
        print(f"{pokemon} has the following moves: ")
        for move in pokemon_moves:
            print(f" {move['move']['name']}")
        if len(pokemon_types) > 1: 
            print(f"{pokemon} can be categorized as the following types: ")
            for type in pokemon_types:
                print(f" {type['type']['name']}")
        else: 
            print (f"{pokemon} is an {pokemon_types[0]['type']['name']} type Pokemon!")

    else:
        print(f"Sorry, we are unable to find {pokemon}, please ensure you have correctly spelled the pokemon's name")
    pokemon = None


