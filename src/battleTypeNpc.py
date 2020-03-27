from npcTemplate import NpcTemplate

class BattleTypeNpc(NpcTemplate):
    def __init__(self, name, sprite, dialog, pokemon=[]):
        super().__init__(name, sprite, dialog)
        self.pokemon = pokemon
        self.currentPokemon = None

    def callPokemon(self, currentPokemon, replacementPokemon):
        if currentPokemon == None:
            currentPokemon == pokemon[0]
            #place pokemon on trainer side of the battlefield

