from normalTemplate import NormalTemplate

def Slash(NormalTemplate):
    def __init__(self, name="slash", moveType="attack", pwr=70, acc=1, pp=20, targets=1, description="The target is attacked with a slash of claws or blades. Critical hits land more easily."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
