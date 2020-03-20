from ./pokemonTemplate import PokemonTemplate

class Bulbasaur(PokemonTemplate):
    def __init__(self, name, nature, level=1, evolveLvl=1, currentExp, totalExp, height=0, weight=0, stats, baseStats currentHp, moves, ailments, catchRate, sprite):
        super().__init__(name, nature, level, evolveLvl, currentExp, totalExp, height, weight, stats, baseStats, currentHp, moves, ailments, catchRate, sprite)

        def evolve(self):
            ivy = new Ivysaur(self, name=self.name, nature=self.nature, level=self.level, evolveLvl=1, currentExp=self.currentExp, totalExp=self.totalExp, height=0, weight=0, stats, baseStats={}, currentHp=1, moves=self.moves, ailments=self.ailments, catchRate=self.catchRate, sprite= "")
            
