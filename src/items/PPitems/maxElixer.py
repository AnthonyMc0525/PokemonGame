class MaxElixer:
    name = "Max Elixer"
    description = "Restores all PP to all moves of a single pokemon."
    function = "PP restore"

    def use(self, pokemon, action):
        for move in pokemon.moves:
            move.currentPP = move.maxPP # increases the pp by 10. may have to change this depending on the structure of pokemon classes
