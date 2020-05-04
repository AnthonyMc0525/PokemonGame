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
player_dialogue_enable = pygame.USEREVENT + 1
player_dialogue_disable = pygame.USEREVENT + 2
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
        self.npc_group= pygame.sprite.Group()
        self.teleport_group= pygame.sprite.Group()
        self.collide=False
        self.dialogue="" # No dialogue by default
        self.interactable=False # Making this ambiguous. But this is a switch to test if NPCs are able to be interacted with.
        self.interacting= False # This is a switch for if the player is currently talking. If they're talking, no moving around.

        self.talk_sprite= (0,0) # Will change co-ordinates as we move around.
        self.pressed= pygame.key.get_pressed()
        self.walls= pygame.sprite.Group()
        self.all_sprites.append(self.player.rect)
        print("Player rect: " + str(self.player.rect))




    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        map_folder = os.path.join(game_folder, '../assets/maps')
        self.map= TiledMap(os.path.join(map_folder, 'arena.tmx'))
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
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name=="player":
                # Player spawn point in the map.
                self.player= Player(self, tile_object.x, tile_object.y)
                print("Spawning player at x:" + str(self.player.vx) + " y: "+ str(self.player.vy) )
            if tile_object.type== "wall":
                self.walls.add(Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
            if tile_object.type=="NPC":
                print("Spawning NPC " + tile_object.name)
                npc_name= tile_object.__dict__['properties']['spawn_name']
                npc_dialogue= tile_object.__dict__['properties']['dialogue']
                # to generate images...

                # game, x, y, w, h, name, sprite, dialog
                self.npcs.append(NpcTemplate(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.name, npc_name.lower(), npc_dialogue))
                # To test collision.
                self.npc_group.add(NpcTemplate(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.name, npc_name.lower(), npc_dialogue))
            if tile_object.type=="teleport":
                map_name= tile_object.__dict__['properties']['to']
                self.teleport_group.add(Teleport(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, map_name))
        self.run()


    def draw_player(self):
        pass

    def run(self):
        print("Game is running...")
        self.playing= True
        while self.playing:
            self.dt= self.clock.tick(FPS)/ 1000.0
            self.update()
            self.draw()
            self.events()

    def dial (self, dial):
        # print("Dialogue: " +dial)
        game_folder = os.path.dirname(__file__)
        assets_folder = os.path.join(game_folder, '../assets')
        blackBarRectPos = (5, self.screen.get_width()-110) # For now.
        blackBarRectSize= (self.screen.get_width()-10, 100)
        pygame.draw.rect(self.screen, KINDA_BLACK, pygame.Rect(blackBarRectPos, blackBarRectSize))
        # font = pygame.font.Font('freesansbold.ttf', 14)
        font = pygame.font.Font(path.join(assets_folder, 'pixelmix.ttf'), 12)
        if isinstance(dial, str):
            try:
                str_arr1=dial.split("%")
            except:
                # Might not have any new window delimiters.
                str_arr1=dial
            for index, s in enumerate(str_arr1):
              str_arr1[index] = s.split("|")
            self.dialogue= str_arr1
            dial= str_arr1
        X = self.screen.get_width()
        Y = self.screen.get_height() + 375
        counter=Y

        for index, s in enumerate(dial[0]):
            text = font.render(dial[0][index], True, WHITE)
            textRect = text.get_rect()
            textRect.center = (X // 2, counter // 2)
            self.screen.blit(text, textRect)
            counter += 40
            # print(str_arr1[0][index])
        # text = font.render(dial, True, WHITE)
        speech_bubble= pygame.image.load(path.join(game_folder, '../assets/images/talk_bubble.png')).convert_alpha()
        self.screen.blit(speech_bubble, self.talk_sprite)

    def events(self):
        # catch all basic events here.
        for event in pygame.event.get():
            try:
                if event== player_dialogue_disable:
                    self.interactable= False
                    self.dialogue=[]
            except:
                pass
            if event.type== pygame.QUIT:
                print("Bye bye...")
                self.quit()
            elif event.type== pygame.KEYDOWN:
                for tele in self.teleport_group:
                              if pygame.sprite.collide_rect(self.player, tele):
                                  pass
                                  # For another time maybe.
                for npc in self.npc_group:
                              if pygame.sprite.collide_rect(self.player, npc):
                                  self.collide= True
                                  if isinstance(npc, NpcTemplate):
                                      # We can do dialogue events here!!
                                      self.interactable= True
                                      self.dialogue= npc.dialog
                                      self.talk_sprite= (npc.x, npc.y - 16)
                                      pygame.time.set_timer(player_dialogue_enable, 0)
                                      pygame.time.set_timer(player_dialogue_disable, 2000)
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
                    if self.interacting==False:
                        self.player.update(event)
                if event.key == pygame.K_ESCAPE:
                    print("See ya!")
                    self.quit()
                elif event.key == pygame.K_SPACE:
                    if self.interactable== True:
                        self.interacting= True
                        self.interactable=False
                    elif self.interacting== True:
                        # They pressed space to continue or cancel.
                        # print(len(self.dialogue))
                        if (len(self.dialogue)) > 1:
                            self.dialogue.pop(0)
                        else:
                            self.interacting= False
                            self.interactable= False


    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        pass


    def draw(self):
        size= [self.width,self.height]
        screen= pygame.display.set_mode(size)
        self.screen.blit(self.map_img, (0, 0))
        for char in self.npcs:
            self.screen.blit(char.image, (char.vx, char.vy))
        self.screen.blit(self.player.image, (self.player.vx, self.player.vy))
        #  Lighting!
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../assets/images')
        light=pygame.image.load(path.join(img_folder, 'circle.png'))
        filter = pygame.surface.Surface(size)
        # filter.fill(pygame.color.Color('Grey'))
        filter.fill(pygame.color.Color(120,128,132))
        filter.blit(light, (self.player.vx-56, self.player.vy-40))
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        #  Test for dialogue here for some reason? Draw dialogue here like it was commented before

        # pygame.draw.rect(self.screen, BLACK, (0, SCREEN_HEIGHT/6, SCREEN_WIDTH, SCREEN_HEIGHT/6))
        if self.interacting== True:
            self.dial(self.dialogue)
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
