from grassTemplate import GrassTemplate

def VineWip(GrassTemplate):
    def __init__(self, name="vine wip", moveType="grass", pwr=45, acc=1, pp=25, targets=1, description="The target is struck with slender, whiplike vines to inflict damage."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


