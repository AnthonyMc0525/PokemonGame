class Potion:
    name = "Potion"
    description = "Restores 200 HP to a single pokemon"
    function = "health restore"

    def use(self, pokemon):
        if(pokemon.currentHp + 200 > pokemon.maxHp):
            pokemon.currentHp = pokemon.maxHp
        else:
            pokemon.currentHp += 200

    def showDescription(self):
        print(self.description)
