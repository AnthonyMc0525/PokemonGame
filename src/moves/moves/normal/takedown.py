from normalTemplate import NormalTemplate
import math

def TakeDown(NormalTemplate):
    def __init__(self, name="take down", moveType="attack", pwr=90, acc=.85, pp=20, targets=1, description="A reckless, full-body charge attack for slamming into the target. This also damages the user a little."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        user.hp -= math.ceil(user.hp * .05)
