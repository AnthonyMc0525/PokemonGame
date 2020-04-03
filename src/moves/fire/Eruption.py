from . import fireTemplate

def Eruption(FireTemplate):
    def __init__(self, name="eruption", moveType="attack", pwr=150, acc=1, pp=5, targets=1, description="The user attacks opposing Pokémon with explosive fury. The lower the user's HP, the lower the move's power."):
    super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        currpwr = (user.currentHp/user.maxHp)*pwr
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
        damage = (((((2*user.lvl)/5 + 2)*currpwr*(user.spAttack/target.spDef))/50)+2) * modifier
        target.changeHp(-damage);

