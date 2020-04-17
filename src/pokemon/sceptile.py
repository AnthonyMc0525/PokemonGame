from pokemon.pokemonTemplate import PokemonTemplate

class Sceptile(PokemonTemplate):
    def __init__(self, name="sceptile", stats={'hp': 70, 'Attack': 85, 'Defense': 65, 'Sp. Atk': 105, 'Sp. Def': 85, 'Speed': 120}, currentHp=250, moves=[], ailments=[]):
        super().__init__(name, currentHp, moves, ailments, stats)
