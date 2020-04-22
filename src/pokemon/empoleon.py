from pokemon.pokemonTemplate import PokemonTemplate

class Empoleon(PokemonTemplate):
    def __init__(self, name="empoleon", type='water', stats={'hp': 84, 'Attack': 86, 'Defense': 88, 'Sp. Atk': 111, 'Sp. Def': 101, 'Speed': 60}, currentHp=278, moves=[], ailments=[]):
        super().__init__(name, type, currentHp, moves, ailments, stats)
