from . import rockTemplate

def Rollout(RockTemplate):
    def __init__(self, name="rollout", moveType="attack", pwr=30, acc=.9, pp=20, targets=1, description="The user continually rolls into the target over five turns. It becomes more powerful each time it hits."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


