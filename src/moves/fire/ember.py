from . import fireTemplate

def Ember(FireTemplate):
    def __init__(self, name="ember", moveType="attack", pwr=40, acc=1, pp=25, targets=1, description="The target is attacked with small flames. This may also leave the target with a burn."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


