from . import dragonTemplate
import random

def DoubleEdge(DragonTemplate):
    def __init__(self, name="dragon breath", moveType="attack", pwr=60, acc=1, pp=20, targets=1, description="The user exhales a mighty gust that inflicts damage. This may also leave the target with paralysis.
"):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
        
        found = False
        for ailment in target.ailments:
            if ailment == "paralyze":
                found = True

        if !found:
            chance = random.randint(0, 100)
            if chance >=70:
                target.ailments.append("paralyze")
