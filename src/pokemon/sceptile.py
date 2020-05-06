from pokemon.pokemonTemplate import PokemonTemplate

class Sceptile(PokemonTemplate):
    def __init__(self, name="sceptile", type='grass', currentHp=250, moves=[], ailments=[], stats={'hp': 70, 'Attack': 85, 'Defense': 65, 'Sp. Atk': 105, 'Sp. Def': 85, 'Speed': 120}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
