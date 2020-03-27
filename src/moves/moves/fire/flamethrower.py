from fireTemplate import FireTemplate

def Flamethrower(FireTemplate):
    def __init__(self, name="flamethrower", moveType="attack", pwr=90, acc=1, pp=15, targets=1, description="The target is scorched with an intense blast of fire. This may also leave the target with a burn."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


