class Potion:
    name = "Potion"
    description = "Restores 20 HP to a single pokemon"
    function = "health restore"

    def use(self, pokemon):
        if(pokemon.currentHp + 20 > pokemon.maxHp):
            pokemon.currentHp = pokemon.maxHp
        else:
            pokemon.currentHp += 20

    def showDescription(self):
        print(self.description)
