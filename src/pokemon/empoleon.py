from . import pokemonTemplate

class Empoleon(PokemonTemplate):
    def __init__(self, name="Empoleon", stats={'hp': 84, 'Attack': 86, 'Defense': 88, 'Sp. Atk': 111, 'Sp. Def': 101, 'Speed': 60}, currentHP=278, moves, ailments=[], sprite):
        super().__init__(name, stats, currentHp, moves, ailments, sprite)
