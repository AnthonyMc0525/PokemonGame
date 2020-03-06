from itemTemplate import ItemTemplate

class PokeBall(ItemTemplate):
    pokemon = None
    rate = []
    def __init__(self, name, description, function, sprite, rate):
        super().__init__(name, description, funtion, sprite)
        self.rate = rate

    def use(self, pokemon):
        ballRoll = randint(self.rate[0], self.rate[1])
        if(pokemon.ailment == "frozen") {
            if(ballRoll + 25 >= pokemon.catchRate){
                self.pokemon = pokemon
                print("You have successfully caught the wild " + pokemon.name)
            } else{
                print("Failed to catch the wild " + pokemon.name.)
            }
        } elif(pokemon.ailment == "paralyzed" ||pokemon.ailment == "burned" ||pokemon.ailment == "poisoned"){
            if(ballRoll + 12 >= pokemon.catchRate){
                self.pokemon = pokemon
                print("You have successfully caught the wild " + pokemon.name)
            } else{
                print("Failed to catch the wild " + pokemon.name.)
            }
            
        } elif(pokemon.ailment == None){
            if(ballRoll >= pokemon.catchRate){
                self.pokemon = pokemon
                print("You have successfully caught the wild " + pokemon.name)
            }
        }
