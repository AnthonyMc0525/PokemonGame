class Ether:
    name = "Ether"
    description = "Restores 10 PP to a single move."
    function = "PP restore"

    def use(self, pokemon, action):
        for move in pokemon.moves:
            if(move = action):
                move.currentPP += 10 # increases the pp by 10. may have to change this depending on the structure of pokemon classes
