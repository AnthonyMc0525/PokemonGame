import random

from . import steelTemplate

def FlashCannon(SteelTemplate):
    def __init__(self, name="flash cannon", moveType="attack", pwr=80, acc=1, pp=10, targets=1, description="The user gathers all its light energy and releases it at once. It may also lower the target's Sp. Def stat."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        chance = random.randint(0, 100)
        if chance > 90:
            #temporarilly change the targets special defense
            pass
