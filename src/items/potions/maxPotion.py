class Potion:
    name = "Potion"
    description = "Restores all HP of a single pokemon"
    function = "health restore"

    def use(self, pokemon):
        pokemon.currentHp = pokemon.maxHp 

    def showDescription(self):
        print(self.description)
