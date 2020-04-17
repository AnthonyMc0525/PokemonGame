from . import grassTemplate

def MagicalLeaf(GrassTemplate):
    def __init__(self, name="magical leaf", moveType="attack", pwr=60, acc=1, pp=20, targets=1, description="The user scatters curious leaves that chase the target. This attack will not miss."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


