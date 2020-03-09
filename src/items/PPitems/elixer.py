class Elixer:
    name = "Elixer"
    description = "Restores 10 PP to all moves of a single pokemon."
    function = "PP restore"

    def use(self, pokemon, action):
        for move in pokemon.moves:
            move.currentPP += 10 # increases the pp by 10. may have to change this depending on the structure of pokemon classes
