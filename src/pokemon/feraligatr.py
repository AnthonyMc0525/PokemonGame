from pokemon.pokemonTemplate import PokemonTemplate

class Feraligatr(PokemonTemplate):
    def __init__(self, name="feraligatr", type='water', currentHp=280, moves=[], ailments=[], stats={'hp': 85, 'Attack': 105, 'Defense': 100, 'Sp. Atk': 79, 'Sp. Def': 83, 'Speed': 78}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
