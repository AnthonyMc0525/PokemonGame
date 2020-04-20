from . import grassTemplate

def RazorLeaf(GrassTemplate):
    def __init__(self, name="razor leaf", moveType="grass", pwr=55, acc=.95, pp=25, targets=1, description="Sharp-edged leaves are launched to slash at opposing Pokémon. Critical hits land more easily."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


