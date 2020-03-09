class MasterBall:
    name = "MasterBall"
    description = "The ultimate pokeball. garuntees the capture of the pokemon it is used on."
    function = "catch"
    pokemon = None

    def use(self, pokemon):
        self.pokemon = pokemon
