import moves.moveTemplate

def FairyTemplate(MoveTemplate):
    def __init__(self, name, moveType, pwr, acc, pp, targets, description):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        if user.type = "fairy":
            stab = 1.5
        else:
            stab = 1

        if target.type == "fighting" or target.type == "dragon" or target.type == "dark":
            eff = 2.0
        else if target.type == "poison" or target.type == "steel":
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff
        damage = (((((2*user.lvl)/5 + 2)*self.pwr*(user.spAttack/target.spDef))/50)+2) * modifier
        target.changeHp(-damage);
