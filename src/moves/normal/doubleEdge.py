from . import normalTemplate
import math

def DoubleEdge(NormalTemplate):
    def __init__(self, name="double-edge", moveType="attack", pwr=120, acc=1, pp=15, targets=1, description="A reckless, life-risking tackle in which the user rushes the target. This also damages the user quite a lot."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        user.hp -= math.ceil(user.hp * .09)
