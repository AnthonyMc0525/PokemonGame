from pokemon.pokemonTemplate import PokemonTemplate

class Venusaur(PokemonTemplate):
    def __init__(self, name="Venusaur", stats={'hp': 80, 'Attack': 82, 'Defense': 83, 'Sp. Atk': 100, 'Sp. Def': 100, 'Speed': 80}, currentHP=270, moves=[], ailments=[]):
        super().__init__(name, stats, currentHp, moves, ailments)
