from moves.water.waterTemplate import WaterTemplate

class AquaTail(WaterTemplate):
    def __init__(self, name="aqua tail", moveType="attack", pwr=90, acc=.9, pp=10, targets=1, description="The user attacks by swinging its tail as if it were a vicious wave in a raging storm."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)
