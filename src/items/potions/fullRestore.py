class Potion:
    name = "Full Restore"
    description = "Restores all HP of a single pokemon and removes all negative statis ailments"
    function = "health restore"

    def use(self, pokemon):
        pokemon.currentHp = pokemon.maxHp 
        pokemon.ailments = None

    def showDescription(self):
        print(self.description)
