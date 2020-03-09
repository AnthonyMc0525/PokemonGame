class Antidote:
    name = "Antidote"
    description = "Cures poison on a single pokemon"
    function = "clear ailment"

    def use(self, pokemon):
        for ailment in pokemon.ailments:
            if(ailment = "poison"):
                pokemon.ailments.remove("poison")
