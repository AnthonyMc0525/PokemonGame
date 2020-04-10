from . import fireTemplate

def FlameCharge(FireTemplate):
    def __init__(self, name="flame charge", moveType="attack", pwr=50, acc=1, pp=20, targets=1, description="Cloaking itself in flame, the user attacks. Then, building up more power, the user raises its Speed stat."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
        #temporarily raise user's speed
