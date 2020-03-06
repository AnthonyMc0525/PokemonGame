class MaxEther:
    name = "Max Ether"
    description = "Restores all PP to a single move."
    function = "PP restore"

    def use(self, pokemon, action):
        for move in pokemon.moves:
            if(move = action):
                move.currentPP = move.maxPP # increases the pp by 10. may have to change this depending on the structure of pokemon classes
