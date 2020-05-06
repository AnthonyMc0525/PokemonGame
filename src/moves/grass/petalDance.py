from moves.grass.grassTemplate import GrassTemplate

class PetalDance(GrassTemplate):
    def __init__(self, name="petal dance", moveType="grass", pwr=120, acc=1, pp=10, targets=1, description="The user attacks the target by scattering petals for two to three turns. The user then becomes confused."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

