from moves.water.waterTemplate import WaterTemplate

class HydroPump(WaterTemplate):
    def __init__(self, name="hydro pump", moveType="attack", pwr=110, acc=.8, pp=5, targets=1, description="The target is blasted by a huge volume of water launched under great pressure."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
