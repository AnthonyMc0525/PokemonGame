from pokemon.pokemonTemplate import PokemonTemplate


class Blastoise(PokemonTemplate):
    def __init__(self, moves=[], name="blastoise", type='water', stats={'hp': 79, 'Attack': 83, 'Defense': 100, 'Sp. Atk': 85, 'Sp. Def': 105, 'Speed': 78}, currentHp=268, ailments=[]):
        super().__init__(name, type, currentHp, moves, ailments, stats)
