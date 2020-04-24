from pokemon.pokemonTemplate import PokemonTemplate

class Infernape(PokemonTemplate):
    def __init__(self, name="infernape", type='fire', currentHp=262, moves=[], ailments=[], stats={'hp': 76, 'Attack': 104, 'Defense': 71, 'Sp. Atk': 104, 'Sp. Def': 71, 'Speed': 108}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
