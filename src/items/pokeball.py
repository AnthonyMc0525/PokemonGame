from itemTemplate import ItemTemplate

class PokeBall(ItemTemplate):
    name = "PokeBall"
    description = ""
    function = "catch"
    sprite = #path to sprite
    pokemon = None
    bonus = 1.0
    def __init__(self):
        pass

    def use(self, pokemon):
        #critical capture is a thing that is not implemented. may or may not be put in
        
        #get ailment of pokemon and check to see what the bonus is for the ailment
        ailmentBonus = 1.0
        #this gets the in battle modified catch rate(mcr) for the pokemon based on its hp, ailment, and type of ball used
        mcr = ((3*pokemon.maxHp-2*pokemon.currentHp)*pokemon.catchRate*self.bonus*ailmentBonus)/(3*pokemon.maxHp)

        #this is the shake probabbility(shp). this determines shake by shake to see if a pokemon breaks out per shake
        shp = False
        if(randint(0, 65536) < (65536*(255/mcr)**-0.1875)){
            
            if(randint(0, 65536) < (65536*(255/mcr)**-0.1875)){
                
                if(randint(0, 65536) < (65536*(255/mcr)**-0.1875)){
                    self.pokemon = pokemon
                }
            } else{
                #pokemon breaks out. 
                #play sound and animation
            }
        } else{
            #pokemon breaks out. 
            #play sound and animation
        }
        
