from pokemon.pokemonTemplate import PokemonTemplate

class Meganium(PokemonTemplate):
    def __init__(self, name="Meganium", stats={'hp': 80, 'Attack': 82, 'Defense': 100, 'Sp. Atk': 83, 'Sp. Def': 100, 'Speed': 80}, currentHP=270, moves=[], ailments=[]):
        super().__init__(name, stats, currentHP, moves, ailments)
