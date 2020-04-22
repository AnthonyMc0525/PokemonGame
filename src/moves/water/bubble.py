from moves.water.waterTemplate import WaterTemplate

class Bubble(WaterTemplate):
    def __init__(self, name="bubble", moveType="water", pwr=40, acc=1, pp=30, targets=1, description="A spray of countless bubbles is jetted at the opposing Pokémon. This may also lower their Speed stat."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
