class PokemonTemplate:
    def __init__(self, name, nature, level=1, evolveLvl=1, currentExp, totalExp, height=0, weight=0, stats={}, baseStats={}, currentHp, moves, ailments, catchRate, sprite):
        self.name = name
        self.nature = nature
        self.level = level
        self.evolveLvl = evolveLvl
        self.currentExp = currentExp
        self.totalExp = totalExp
        self.height = 0
        self.weight = 0
        self.stats = stats
        self.baseStats = baseStats
        self.currentHp = currentHp
        self.moves = moves
        self.ailments = ailments
        self.catchRate = catchRate
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
        self.hp = amount

    def lvlUp(self):
        for key, value in stats.items()
            self.level += 1
            if(key != hp):
                stats[key] = floor(floor((2 * baseStat[key]) * self.level / 100 + 5) * self.nature) # (+ I + E) would be added directly after baseStat in the ()  if we would include IV's and EV's into the game
            elif(key == hp):
                stats[key] = floor((2 * baseStat[key]) * self.level / 100 + self.level + 10) # (+ I + E) would be added directly after baseStat in the () if we would include IV's and EV's into the game

        #if the pokemon is supposed to evolve at this level, show prompt that the pokemon is evolving.
        if(self.level == evolveLvl):
            #for the actual pokemon classes they will have an evolve method that does the heavy lifting for this if statment
            self.evolve()

        #if the pokemon is supposed to learn a move this level then give player the option to teach the pokemon the move here
        for lvl, move in learnableMoves.items():
            if(self.level == lvl):
                print(self.name + " wants to learn " + move + ".")
                print("press a move to replace")
                #if player clicks move
                    #prompt them to make sure that is what they want to do
                        #if player clicks yes
                            #replace moves
                        #else
                            #do nothing
