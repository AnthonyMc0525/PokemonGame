from . import grassTemplate

def SolarBeam(GrassTemplate):
    def __init__(self, name="solar beam", moveType="grass", pwr=120, acc=1, pp=10, targets=1, description="In this two-turn attack, the user gathers light, then blasts a bundled beam on the next turn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


