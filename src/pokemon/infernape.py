from pokemon.pokemonTemplate import PokemonTemplate

class Infernape(PokemonTemplate):
    def __init__(self, name="infernape", stats={'hp': 76, 'Attack': 104, 'Defense': 71, 'Sp. Atk': 104, 'Sp. Def': 71, 'Speed': 108}, currentHp=262, moves=[], ailments=[]):
        super().__init__(name, currentHp, moves, ailments, stats)
