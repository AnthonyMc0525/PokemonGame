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
