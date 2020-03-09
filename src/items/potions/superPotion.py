class SuperPotion:
    name = "Super Potion"
    description = "Restores 50 HP to a single pokemon"
    function = "health restore"

    def use(self, pokemon):
        if(pokemon.currentHp + 50 > pokemon.maxHp):
            pokemon.currentHp = pokemon.maxHp
        else:
            pokemon.currentHp += 50

    def showDescription(self):
        print(self.description)
