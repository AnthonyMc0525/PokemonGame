import math

from moves.moveTemplate import MoveTemplate

class FireTemplate(MoveTemplate):
    def __init__(self, name, moveType, pwr, acc, pp, targets, description):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        if user.type == "fire":
            stab = 1.5
        else:
            stab = 1

        if target.type == "grass" or target.type == "ice" or target.type == "bug" or target.type == "steel":
            eff = 2.0
        elif target.type == "water" or target.type == "ground" or target.type == "rock": 
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff
        damage = math.floor(((((2*100)/5 + 2)*self.pwr*(user.stats['Sp. Atk']/target.stats['Sp. Def']))/50)+2) * modifier
        print(damage)
        if target.currentHp - damage <= 0:
            target.currentHp = 0
        else:
            target.currentHp -= damage
