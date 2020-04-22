from moves.fire.fireTemplate import FireTemplate

class FlameWheel(FireTemplate):
    def __init__(self, name="flame wheel", moveType="fire", pwr=60, acc=1, pp=25, targets=1, description="The user cloaks itself in fire and charges at the target. This may also leave the target with a burn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        found = False
        for ailment in target.ailments:
            if ailment == "burn":
                found = True

        if not found:
            chance = random.randint(0, 100)
            if chance > 90:
                target.ailments.append("burn")
