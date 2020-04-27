from moves.fire.fireTemplate import FireTemplate

class Eruption(FireTemplate):
    def __init__(self, name="eruption", moveType="fire", pwr=150, acc=1, pp=5, targets=1, description="The user attacks opposing Pokémon with explosive fury. The lower the user's HP, the lower the move's power."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user,target)
