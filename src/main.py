import sys
import os
import random

# ---- #

import pygame as pygame
from pygame.locals import *
import pytmx.util_pygame
#import load_pygame
import numpy as np

# --- #

from strings import *
from tiledmap import *
# from player import *
from sprites import *
from npcTemplate import *
from battleTypeNpc import *
# --- #
#
map_x=0
map_y=0
#
class Game:
#
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        size= [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen= pygame.display.set_mode(size)
        self.screen.fill(BLACK)
        pygame.display.set_caption(GAME_NAME)
        self.clock= pygame.time.Clock()
        self.running= True
        self.load_data()
        self.player= Player(self, 0, 0)
        self.all_sprites= []
        self.npcs=[]
        self.all_sprites.append(self.player.rect)
        print("Player rect: " + str(self.player.rect))
        # self.all_sprites= pygame.sprite.Group()
        print("Initialised game.")


    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        map_folder = os.path.join(game_folder, '../assets/maps')
        self.map= TiledMap(os.path.join(map_folder, 'betamap.tmx'))
        self.height = self.map.height
        self.width = self.map.width
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        img_folder = os.path.join(game_folder, 'assets/images')
        item_folder = os.path.join(game_folder, 'assets/items')
        print("Loading " + game_folder)
        print("Map folder: " + map_folder)
        print("Item folder: " +item_folder)
        print("Image folder: "+ img_folder)

    def new(self):
        self.walls= pygame.sprite.Group()
        # self.npcs= pygame.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name=="player":
                # Player spawn point in the map.
                self.player= Player(self, tile_object.x, tile_object.y)
            if tile_object.name== "wall":
                Obstacle(self, tile_object.x, tile_object.y, tile_object.height, tile_object.width)
            if tile_object.type=="NPC":
                print("Spawning NPC " + tile_object.name)
                self.npcs.append(NpcTemplate(self, tile_object.x, tile_object.y, tile_object.name))
                # print("NPC Sprite " + str(new_npc.name) + ": " + str(new_npc.sprite))
                # self.all_sprites.append(self.player)
        self.run()


    def draw_player(self):
        pass

    def run(self):
        print("Game is running...")
        self.playing= True
        while self.playing:
            self.dt= self.clock.tick(FPS)/ 1000.0
            self.events()
            self.update()
            self.draw()
            self.player.update()

    def events(self):
        # catch all basic events here.
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                print("Bye bye...")
                self.quit()
            elif event.type== pygame.KEYDOWN:
                # Key press event. Use this for pause later? Esc will also exit the game until we got a pause menu.
                # print("Detected key press.")
                if event.key == pygame.K_ESCAPE:
                    print("See ya!")
                    self.quit()
    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # self.all_sprites.update()
        pass

    def draw(self):
        size= [self.width,self.height]
        screen= pygame.display.set_mode(size)
        self.screen.blit(self.map_img, (0, 0))
        self.screen.blit(self.player.image, (self.player.vx, self.player.vy))
        for char in self.npcs:
            print("x: " + str(char.vx) + " | y: " + str(char.vy) + "\n")
            # pygame.draw.rect(self.screen, BLACK, (char.x, char.y, 16, 32))

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
    size= [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen= pygame.display.set_mode(size)

    while not done:
        game.new()
        game.run()

    # If done, quit.
    pygame.quit()

if __name__ == "__main__":
    main()
