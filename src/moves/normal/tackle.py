from . import normalTemplate

def Tackle(NormalTemplate):
    def __init__(self, name="tackle", moveType="attack", pwr=40, acc=1, pp=35, targets=1, description="A physical attack in which the user charges and slams into the target with its whole body."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
