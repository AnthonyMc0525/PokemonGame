class MaxRevive:
    name = "MaxRevive"
    description = "restores all hp of a fainted pokemon"
    function = "revive"

    def use(self, pokemon):
        if(pokemon.currentHp != 0):
            print("this item cannot be used on this pokemon at this time.")
        else:
            pokemon.currentHp = pokemon.maxHp
