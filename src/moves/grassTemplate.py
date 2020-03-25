from moveTemplate import MoveTemplate

def GrassTemplate(MoveTemplate):
    def __init__(self, name=" Petal Blizzard", moveType="grass", pwr=90, acc=1, pp=15, targets=2, description="Petal Blizzard does damage to all adjacent Pokémon, including allies.")
    super().__init__(name, moveType, pwr, acc, pp, targets,  description)

    def use(self, user, target):
        if user.type = "grass":
            stab = 1.5
        else:
            stab = 1

        if target.type == "ground" or target.type == "rock" or target.type == "water":
            eff = 2.0
        else if target.type == "fire" or target.type == "ice" or target.type == "poison" or target.type == "flying" or target.type == "bug":
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff


        damage = (((((2*user.lvl)/5 + 2)*self.pwr*(user.spAttack/target.spDef))/50)+2) * modifier

        target.changeHp(-damage);
