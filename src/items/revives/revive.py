class Revive:
    name = "Revive"
    description = "restores half the hp of a fainted pokemon"
    function = "revive"

    def use(self, pokemon):
        if(pokemon.currentHp != 0):
            print("this item cannot be used on this pokemon at this time.")
        else:
            pokemon.currentHp = pokemon.maxHp/2
