from grassTemplate import GrassTemplate

def PetalBlizzard(GrassTemplate):
    def __init__(self, name="petal blizzard", moveType="grass", pwr=90, acc=1, pp=15, targets=2, description="The user stirs up a violent petal blizzard and attacks everything around it."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


