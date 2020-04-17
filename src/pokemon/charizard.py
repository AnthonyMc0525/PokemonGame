from pokemon.pokemonTemplate import PokemonTemplate

class Charizard(PokemonTemplate):
    def __init__(self, name="Charizard", stats={'hp': 78, 'Attack': 84, 'Defense': 78, 'Sp. Atk': 109, 'Sp. Def': 85, 'Speed': 100}, currentHp=266, moves=[], ailments=[]):
        super().__init__(name, stats, currentHp, moves, ailments)
