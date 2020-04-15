from grassTemplate import GrassTemplate

def SeedBomb(GrassTemplate):
    def __init__(self, name="seed bomb", moveType="grass", pwr=80, acc=1, pp=15, targets=1, description="The user slams a barrage of hard-shelled seeds down on the target from above."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


