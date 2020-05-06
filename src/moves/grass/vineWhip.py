from moves.grass.grassTemplate import GrassTemplate

class VineWhip(GrassTemplate):
    def __init__(self, name="vine whip", moveType="grass", pwr=45, acc=1, pp=25, targets=1, description="The target is struck with slender, whiplike vines to inflict damage."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


