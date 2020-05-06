from . import normalTemplate

def Scratch(NormalTemplate):
    def __init__(self, name="scratch", moveType="attack", pwr=40, acc=1, pp=35, targets=1, description="Hard, pointed, sharp claws rake the target to inflict damage."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
