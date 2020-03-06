class ParalyzHeal:
    name = "Paralyz Heal"
    description = "Cures paralysis on a single pokemon"
    function = "clear ailment"

    def use(self, pokemon):
        for ailment in pokemon.ailments:
            if(ailment = "paralysis"):
                pokemon.ailments.remove("paralysis")
