from . import fireTemplate

def FireFang(FireTemplate):
    def __init__(self, name="fire fang", moveType="attack", pwr=65, acc=.95, pp=15, targets=1, description="The user bites with flame-cloaked fangs. This may also make the target flinch or leave it with a burn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)


