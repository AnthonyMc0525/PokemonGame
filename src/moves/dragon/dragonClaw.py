from . import dragonTemplate

def DragonClaw(DragonTemplate):
    def __init__(self, name="dragon claw", moveType="attack", pwr=80, acc=1, pp=15, targets=1, description="The user slashes the target with huge sharp claws."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
