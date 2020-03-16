import sys
from os import path
# ---- #

import pygame
import pytmx

# ---- #
class Game:

    def __init__(self):
        pygame.init()
        self.screen= pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Pokemon Game")
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        img_folder = path.join(game_folder, 'images')
        item_folder = path.join(game_folder, 'items')
        self.map= TiledMap(path.join(map_folder, 'betamap.tmx'))
        self.map_img= self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new (self):
        pass

    def run(self):
        # Game loop.
        self.playing= True
        while self.playing:
            self.dt: self.clock(FPS)/ 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        # TODO: Add camera for drawing tiles.
        pass

    def events(self):
        # catch all basic events here.
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                self.quit()
            elif event.type== pygame.KEYDOWN:
                # Key press event. Use this for pause later? Esc will also exit the game until we got a pause menu.
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

class TiledMap:
    """
    Loads and renders Tiled maps.
    """
    def __init__(self, filename):
        tm= pytmx.load_pygame(filename, pixelalpha= True)
        # Width/Height is how many tiles the map is. The tilewidth/tileheight property is how many pixels the tiles are (Should always be 16 but just in case...)
        self.width= tm.width * tm.tilewidth
        self.height= tm.height * tm.tileheight
        self.tmxdata= tm

    def render(self, surface):
        ti= self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                # We need co-ords and IDs.
                for x, y, gid, in layer:
                    tile= ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

def main():
    """
    Meat and potatoes of starting up the game.
    """
    game= Game()
    game.show_start_screen()
    while True:
        game.new()
        game.run()
        game.show_go_screen()

if __name__== "__main__":
    main()
