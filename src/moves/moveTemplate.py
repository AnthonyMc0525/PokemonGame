def MoveTemplate:
    def __init__(self, name, moveType, pwr, acc, pp, targets, description):
        self.name = name
        self.type = moveType
        self.pwr = pwr
        self.acc = acc
        self.pp = pp
        self.description = description
        self.targets = targets

    #moves from this template will have to create a use method
