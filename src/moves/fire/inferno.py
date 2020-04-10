from . import fireTemplate

def Inferno(FireTemplate):
    def __init__(self, name="inferno", moveType="attack", pwr=100, acc=.5, pp=5, targets=1, description="The user attacks by engulfing the target in an intense fire. This leaves the target with a burn."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


