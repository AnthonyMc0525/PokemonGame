from pokemon.pokemonTemplate import PokemonTemplate


class Blastoise(PokemonTemplate):
    def __init__(self, name="blastoise", type='water', currentHp=268, moves=[], ailments=[], stats={'hp': 79, 'Attack': 83, 'Defense': 100, 'Sp. Atk': 85, 'Sp. Def': 105, 'Speed': 78}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
