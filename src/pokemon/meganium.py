from pokemon.pokemonTemplate import PokemonTemplate

class Meganium(PokemonTemplate):
    def __init__(self, name="meganium", type='grass', stats={'hp': 80, 'Attack': 82, 'Defense': 100, 'Sp. Atk': 83, 'Sp. Def': 100, 'Speed': 80}, currentHp=270, moves=[], ailments=[]):
        super().__init__(name, type, currentHp, moves, ailments, stats)
