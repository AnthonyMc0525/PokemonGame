from pokemon.pokemonTemplate import PokemonTemplate

class Swampert(PokemonTemplate):
    def __init__(self, name="swampert", stats={'hp': 100, 'Attack': 110, 'Defense': 90, 'Sp. Atk': 85, 'Sp. Def': 90, 'Speed': 60}, currentHp=310, moves=[], ailments=[]):
        super().__init__(name, currentHp, moves, ailments, stats)
