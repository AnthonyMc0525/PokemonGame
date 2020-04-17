from pokemon.pokemonTemplate import PokemonTemplate

class Torterra(PokemonTemplate):
    def __init__(self, name="torterra", stats={'hp': 95, 'Attack': 109, 'Defense': 105, 'Sp. Atk': 75, 'Sp. Def': 85, 'Speed': 56}, currentHp=300, moves=[], ailments=[]):
        super().__init__(name, currentHp, moves, ailments, stats)
