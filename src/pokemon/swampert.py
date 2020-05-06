from pokemon.pokemonTemplate import PokemonTemplate

class Swampert(PokemonTemplate):
    def __init__(self, name="swampert", type='water', currentHp=310, moves=[], ailments=[], stats={'hp': 100, 'Attack': 110, 'Defense': 90, 'Sp. Atk': 85, 'Sp. Def': 90, 'Speed': 60}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
