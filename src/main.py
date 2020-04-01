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
        self.pressed= pygame.key.get_pressed()
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
                npc_name= tile_object.name
                self.npcs.append(NpcTemplate(self, tile_object.x, tile_object.y, npc_name.lower()))
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


    def events(self):
        # catch all basic events here.
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                print("Bye bye...")
                self.quit()
            elif event.type== pygame.KEYDOWN:
                self.player.update(event)
                # Key press event. Use this for pause later? Esc will also exit the game until we got a pause menu.
                # print("Detected key press.")
                if event.key == pygame.K_ESCAPE:
                    print("See ya!")
                    self.quit()
                elif event.key == pygame.K_SPACE:
                    print("AAAAAA")
                    pygame.draw.rect(self.screen, BLACK, (10, 10, 50, 50))
                    # self.player.dialogue(event, "TEST TEXT")

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # self.all_sprites.update()
        pass

    def dialogue (self, dial):
        screen= self.screen

        blackBarRectPos = (5, screen.get_width()-110) # For now.
        blackBarRectSize= (screen.get_width()-10, 100)
        pygame.draw.rect(screen, BLACK, pygame.Rect(blackBarRectPos, blackBarRectSize))
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(dial, True, WHITE, BLACK)
        textRect = text.get_rect()
        X = screen.get_width()
        Y = screen.get_height() + 375
        textRect.center = (X // 2, Y // 2)
        screen.blit(text, textRect)

    def draw(self):
        size= [self.width,self.height]
        screen= pygame.display.set_mode(size)
        self.screen.blit(self.map_img, (0, 0))
        for char in self.npcs:
            self.screen.blit(char.image, (char.vx, char.vy))
        self.screen.blit(self.player.image, (self.player.vx, self.player.vy))

        #  Test for dialogue here for some reason? Draw dialogue here like it was commented before


        # self.dialogue('Hello World')
        # pygame.draw.rect(self.screen, BLACK, (0, SCREEN_HEIGHT/6, SCREEN_WIDTH, SCREEN_HEIGHT/6))

        # Draw dialogue??

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
