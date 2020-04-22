from moves.water.waterTemplate import WaterTemplate

class WaterGun(WaterTemplate):
    def __init__(self, name="water gun", moveType="attack", pwr=40, acc=1, pp=25, targets=1, description="The target is blasted with a forceful shot of water."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
