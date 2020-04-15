from . import darkTemplate
import random

def Bite(DarkTemplate):
    def __init__(self, name="bite", moveType="attack", pwr=60, acc=1, pp=25, targets=1, description="The target is bitten with viciously sharp fangs. This may also make the target flinch."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        found = False
        for ailment in target.ailments:
            if ailment == "flinch":
                found = True

        if !found:
            chance = random.randint(0, 100)
            if chance > 90:
                target.ailments.append("flinch")
