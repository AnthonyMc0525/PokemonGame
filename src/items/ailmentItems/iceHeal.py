class IceHeal:
    name = "Ice Heal"
    description = "Cures frozen on a single pokemon"
    function = "clear ailment"

    def use(self, pokemon):
        for ailment in pokemon.ailments:
            if(ailment = "frozen"):
                pokemon.ailments.remove("frozen")
