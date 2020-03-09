class Awakening:
    name = "Antidote"
    description = "Cures sleep on a single pokemon"
    function = "clear ailment"

    def use(self, pokemon):
        for ailment in pokemon.ailments:
            if(ailment = "sleep"):
                pokemon.ailments.remove("sleep")
