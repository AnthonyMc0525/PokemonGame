from moves.water.waterTemplate import WaterTemplate

class WaterPulse(WaterTemplate):
    def __init__(self, name="water pulse", moveType="attack", pwr=60, acc=1, pp=20, targets=1, description="The user attacks the target with a pulsing blast of water. This may also confuse the target."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)

        found = False
        for ailment in target.ailments:
            if ailment == "confused":
                found = True

        if not found:
            chance = random.randint(0, 100)
            if chance > 80:
                target.ailments.append("confused")
