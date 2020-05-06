from moves.fire.fireTemplate import FireTemplate

class FireSpin(FireTemplate):
    def __init__(self, name="fire spin", moveType="fire", pwr=35, acc=.85, pp=15, targets=1, description="The target becomes trapped within a fierce vortex of fire that rages for four to five turns."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


