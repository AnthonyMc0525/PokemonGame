from . import flyingTemplate

def AirSlash(FlyingTemplate):
    def __init__(self, name="air slash", moveType="attack", pwr=75, acc=.95, pp=15, targets=1, description="The user attacks with a blade of air that slices even the sky. This may also make the target flinch."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
