from moveTemplate import MoveTemplate

def FireTemplate(MoveTemplate):
    def __init__(self, name, moveType="fire", pwr, acc, pp, targets, burn, description):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)
        self.burn = burn

    def use(self, user, target):
        if user.type = "fire":
            stab = 1.5
        else:
            stab = 1

        if target.type == "grass" or target.type == "ice" or target.type == "bug" or target.type == "steel":
            eff = 2.0
        else if target.type == "water" or target.type == "ground" or target.type == "rock": 
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff
        damage = (((((2*user.lvl)/5 + 2)*self.pwr*(user.spAttack/target.spDef))/50)+2) * modifier
        target.changeHp(-damage);

        found = False
        for ailment in target.ailments
            if ailment = "burn":
                found = True

        if !found:
           ailments.append("burn") 
