class BurnHeal:
    name = "Burn Heal"
    description = "Cures burn on a single pokemon"
    function = "clear ailment"

    def use(self, pokemon):
        for ailment in pokemon.ailments:
            if(ailment = "burn"):
                pokemon.ailments.remove("burn")
