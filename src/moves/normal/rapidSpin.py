from . import NormalTemplate

def Tackle(NormalTemplate):
    def __init__(self, name="rapid spin", moveType="attack", pwr=50, acc=1, pp=40, targets=1, description="A spin attack that can also eliminate such moves as Bind, Wrap, and Leech Seed. This also raises the user's Speed stat."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
