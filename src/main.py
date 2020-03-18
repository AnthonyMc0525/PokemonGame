import sys
import os as path
# ---- #

import pygame as pygame
from pygame.locals import *
import pytmx.util_pygame import load_pygame
import cv2
import numpy as np

# --- #

from strings import *
from tiledmap import *
from player import *
# --- #

map_x=0
map_y=0

class Game:

    def __init__(self):
        pygame.init()
        size= [SCREEN_WIDTH,SCREEN_HEIGHT]
        self.screen= pygame.display.set_mode(size)
        self.screen.fill(BLACK)
        pygame.display.set_caption(GAME_NAME)
        self.clock= pygame.time.Clock()
        self.load_data()
        print("Initialised game.")


    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

    def load_data(self):
        game_folder = path.dirname(__file__)[0:-3]
        map_folder = path.join(game_folder, 'assets/maps')
        img_folder = path.join(game_folder, 'assets/images')
        item_folder = path.join(game_folder, 'assets/items')
        print("Loading " + game_folder)
        print("Map folder: " + map_folder)
        print("Item folder: " +item_folder)
        print("Image folder: "+ img_folder)
        # self.map= TiledMap(path.join(map_folder, 'betamap.tmx'))

        # https://pytmx.readthedocs.io/en/latest/
        # Help please god
        tmxdata= load_pygame(path.join(map_folder, 'betamap.tmx')
        self.clock= pygame.time.Clock()

    def new (self):
        # pass
        self.player= Player()
        print("Player spawned.")


    def run(self):
        print("Game is running...")
        self.playing= True
        while self.playing:
            self.dt= self.clock.tick(FPS)/ 1000.0
            self.events()
            self.update()
            self.draw()

    def events(self):
        # catch all basic events here.
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                print("Bye bye...")
                self.quit()
            elif event.type== pygame.KEYDOWN:
                # Key press event. Use this for pause later? Esc will also exit the game until we got a pause menu.
                print("Detected key press.")
                if event.key == pygame.K_ESCAPE:
                    print("See ya!")
                    self.quit()
    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        size= [SCREEN_WIDTH,SCREEN_HEIGHT]
        screen= pygame.display.set_mode(size)
        # Limit to 60 fps
        clock= pygame.time.Clock()
        clock.tick(FPS)
        pygame.display.flip()
        #  blit the screen?



def main():
    """
    Main program to jump start.
    """
    pygame.init()
    pygame.display.set_caption(GAME_NAME)
    done= False
    game=Game()
    while not done:
        game.new()
        game.run()

    # If done, quit.
    pygame.quit()

if __name__ == "__main__":
    main()
