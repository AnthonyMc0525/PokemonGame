class PokemonTemplate:
    def __init__(self, name, height=0, weight=0, stats={}, currentHp, moves, ailments, sprite):
        self.name = name
        self.height = 0
        self.weight = 0
        self.stats = stats
        self.baseStats = baseStats
        self.currentHp = currentHp
        self.moves = moves
        self.ailments = ailments
        self.sprite = sprite


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

