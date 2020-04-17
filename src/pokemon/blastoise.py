from pokemon.pokemonTemplate import PokemonTemplate


class Blastoise(PokemonTemplate):
    def __init__(self, moves=[], name="Blastoise", stats={'hp': 79, 'Attack': 83, 'Defense': 100, 'Sp. Atk': 85, 'Sp. Def': 105, 'Speed': 78}, currentHP=268, ailments=[]):
        super().__init__(name, stats, currentHp, moves, ailments)
