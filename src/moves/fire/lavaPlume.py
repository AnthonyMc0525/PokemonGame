from . import fireTemplate

def LavaPlume(FireTemplate):
    def __init__(self, name="lava plume", moveType="attack", pwr=80, acc=1, pp=15, targets=2, description="The user torches everything around it in an inferno of scarlet flames. This may also leave those it hits with a burn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        found = False
        for ailment in target.ailments:
            if ailment == "burn":
                found = True

        if !found:
            chance = random.randint(0, 100)
            if chance > 90:
                target.ailments.append("burn")
