class PokemonTemplate:
    def __init__(self, name,type, currentHp, moves, ailments, stats={}):
        self.name = name
        self.stats = stats
        self.currentHp = currentHp
        self.moves = moves
        self.ailments = ailments
        self.type= type


    def addAilment(self, ailment):
        self.ailments.add(ailment)

    def useMove(self, num, target):
        if self.moves[num].pp == 0:
            print("you do not have enough PP for that move")
        else:
            self.moves[num].use(target)

    def changeHp(self, amount):
        #amount is negative if the pokemon loses hp. positive if they gain hp
        if self.currentHp + amount < 0:
            self.currentHp = 0
        self.currenthp += amount
