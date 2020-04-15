from . import normalTemplate

def SkullBash(NormalTemplate):
    def __init__(self, name="skull bash", moveType="attack", pwr=130, acc=1, pp=10, targets=1, description="The user tucks in its head to raise its Defense stat on the first turn, then rams the target on the next turn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
