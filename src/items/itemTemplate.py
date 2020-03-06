class ItemTemplate:
    name = ""
    description = ""
    function = "" #this will be what this thing does in game
    sprite = "" #this will be where the sprite is held for the item

    def __init__(self, name, description, function, sprite):
        self.name = name
        self.description = description
        self.function = function
        self.sprite = sprite

    def use(self, target):
        #uses the item
        pass

    def showDescription(self):
        # used for desplaying what the item does in game
        print(description)
