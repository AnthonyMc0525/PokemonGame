from . import normalTemplate

def QuickAttack(NormalTemplate):
    def __init__(self, name="quick attack", moveType="attack", pwr=40, acc=1, pp=30, targets=1, description="The user lunges at the target at a speed that makes it almost invisible. This move always goes first."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
