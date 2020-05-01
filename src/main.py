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
        self.collide=False
        self.pressed= pygame.key.get_pressed()
        self.walls= pygame.sprite.Group()
        self.all_sprites.append(self.player.rect)
        print("Player rect: " + str(self.player.rect))
        print("Initialised game.")


    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        map_folder = os.path.join(game_folder, '../assets/maps')
        self.map= TiledMap(os.path.join(map_folder, 'gym.tmx'))
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
        # self.walls= pygame.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name=="player":
                # Player spawn point in the map.
                self.player= Player(self, tile_object.x, tile_object.y)
                print("Spawning player at x:" + str(self.player.vx) + " y: "+ str(self.player.vy) )
                # self.walls.add(self.player)
            if tile_object.name== "wall":
                self.walls.add(Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height))

                # print("Spawning wall at x:" +str(tile_object.x) + " y: " + str(tile_object.y) + " h: " + str(tile_object.height) + " w: " + str(tile_object.width))
            if tile_object.type=="NPC":
                print("Spawning NPC " + tile_object.name)
                npc_name= tile_object.__dict__['properties']['spawn_name']
                self.walls.add(NpcTemplate(self, tile_object.x, tile_object.y, tile_object.height, tile_object.width, npc_name.lower()))
                self.npcs.append(NpcTemplate(self, tile_object.x, tile_object.y, tile_object.height, tile_object.width, npc_name.lower()))
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
                #  Check collision with NPCs?

                # I'm so tired of collision. -Danny
                posx = self.player.rect.x
                posy = self.player.rect.y
                # print(posx)

                # for wall in self.walls:
                #     if posx > wall.x and posx < wall.x + wall.width:
                #         if posy > wall.y and posy < wall.y + wall.height:
                #             self.collide=True
                #             print("oi")
                #             break
                #     else:
                #         self.collide=False
                # if self.collide==False:
                #     self.player.update(event)
                # else:
                #     pass

                for wall in self.walls:
                    if pygame.sprite.collide_rect(self.player, wall):
                        self.collide= True
                        # Back up
                        if self.player.dir=="down":
                            self.player.vy -= self.player.speed
                            self.player.rect.y -= self.player.speed
                        elif self.player.dir=="up":
                            self.player.vy += self.player.speed
                            self.player.rect.y += self.player.speed
                        elif self.player.dir=="left":
                            self.player.vx += self.player.speed
                            self.player.rect.x += self.player.speed
                        else:
                            self.player.vx -= self.player.speed
                            self.player.rect.x -= self.player.speed
                    else:
                        self.collide= False


                if self.collide== False:
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

        # for wall in self.walls:
        #     pygame.draw.rect(self.screen, RED, (wall.x, wall.y, wall.width, wall.height))
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
