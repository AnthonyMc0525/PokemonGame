from . import normalTemplate

def BodySlam(NormalTemplate):
    def __init__(self, name="body slam", moveType="attack", pwr=85, acc=1, pp=15, targets=1, description="The user drops onto the target with its full body weight. It may also leave the target with paralysis."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        found = False
        for ailment in target.ailments:
            if ailment == "paralysis":
                found = True

        if !found:
            chance = random.randint(0, 100)
            if chance > 70:
                target.ailments.append("paralysis")
