from pokemon.pokemonTemplate import PokemonTemplate

class Blaziken(PokemonTemplate):
    def __init__(self, name="blaziken", type='fire', stats={'hp': 80, 'Attack': 120, 'Defense': 70, 'Sp. Atk': 110, 'Sp. Def': 70, 'Speed': 80}, currentHp=270, moves=[], ailments=[]):
        super().__init__(name, type, currentHp, moves, ailments, stats)
