from . import fireTemplate

def BurnUp(FireTemplate):
    def __init__(self, name="burn up", moveType="attack", pwr=130, acc=1, pp=5, targets=1, description="To inflict massive damage, the user burns itself out. After using this move, the user will no longer be Fire type."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        user.types.remove("fire")
