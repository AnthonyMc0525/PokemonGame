from moveTemplate import MoveTemplate

def GroundTemplate(MoveTemplate):
    def __init__(self, name, moveType, pwr, acc, pp, targets, description)
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        if user.type = "ground":
            stab = 1.5
        else:
            stab = 1

        if target.type == "fire" or target.type == "electric" or target.type == "poison" or target.type == "rock" or target.type == "steel":
            eff = 2.0
        else if target.type == "water" or target.type == "grass" or target.type == "ice":
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff
        damage = (((((2*user.lvl)/5 + 2)*self.pwr*(user.spAttack/target.spDef))/50)+2) * modifier
        target.changeHp(-damage);
