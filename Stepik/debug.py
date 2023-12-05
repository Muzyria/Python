
print(len(pokemons := [pokemon.strip() for pokemon in __import__('sys').stdin]) - len(set(pokemons)))
