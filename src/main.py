import sys
import os
import random
# ---- #

import pygame as pygame
from pygame.locals import *
import pytmx.util_pygame
#import load_pygame
# import cv2
import numpy as np

# --- #

from strings import *
from tiledmap import *
# from player import *
from sprites import *
from battle import *
# --- #
#
map_x=0
map_y=0
#
pygame.mixer.init()
battleMusic = pygame.mixer.Sound("sounds/battle.wav")
#
class Game:
#
    def __init__(self):
        pygame.init()
        size= [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen= pygame.display.set_mode(size)
        self.screen.fill(BLACK)
        pygame.display.set_caption(GAME_NAME)
        self.clock= pygame.time.Clock()
        self.running= True
        self.load_data()
        self.player= Player()
        self.all_sprites= []
        self.all_sprites.append(self.player.rect)
        self.battling= False
        self.music= pygame.mixer.music.load("sounds/idle.wav")
        # self.all_sprites= pygame.sprite.Group()
        print("Initialised game.")

    def game_intro(self, screen):
        intro = True
        screen.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf',115)
        textSurface = font.render("Start", True, BLACK)
        textRect_start = textSurface.get_rect()
        textRect_start.center = (350, 500)
        screen.blit(textSurface, textRect_start)
        width = textRect_start.width
        height = textRect_start.height
        x = 350 - width/2
        y = 500 - height/2

        small_font = pygame.font.Font('freesansbold.ttf', 30)
        instructions = "When in the game, press 'b' to enter a"
        textSurf = small_font.render(instructions, True, BLACK)
        tRect = textSurf.get_rect()
        tRect.center = (350, 200)
        screen.blit(textSurf, tRect)

        instructions = "battle with random pokemon and moves."
        textSurf2 = small_font.render(instructions, True, BLACK)
        tRect2 = textSurf2.get_rect()
        tRect2.center = (350, 250)
        screen.blit(textSurf2, tRect2)

        instructions = "You will be the pokemon on the left."
        textSurf3 = small_font.render(instructions, True, BLACK)
        tRect3 = textSurf3.get_rect()
        tRect3.center = (350, 300)
        screen.blit(textSurf3, tRect3)
        pygame.display.update()
        self.clock.tick(FPS)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > x and pos[0] < x + width:
                        if pos[1] > y and pos[1] < y + height:
                            self.run() 






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
        self.run()


    def draw_player(self):
        pass

    def run(self):
        # pygame.mixer.music.play(-1)
        print("Game is running...")
        self.playing= True
        while self.playing:
            self.dt= self.clock.tick(FPS)/ 1000.0
            self.events()
            self.update()
            self.draw()
            # self.player.update()

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
                elif event.key == pygame.K_b:
                    if self.battling== False:
                        pygame.mixer.music.fadeout(1000)
                        print("'b' key pressed")
                        batt= Battle(self)
                        batt.main()
                else:
                    if self.battling== False:
                        self.player.update(event)
    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # self.all_sprites.update()
        pass

    def draw(self):
        if self.battling== False:
            size= [self.width,self.height]
            screen= pygame.display.set_mode(size)
            self.screen.blit(self.map_img, (0, 0))
            self.screen.blit(self.player.image, (self.player.vx, self.player.vy))

            # pygame.draw.circle(self.screen, WHITE, [30, 30], 30)
            # Make a function to draw the player sprite here!!
            # if not self.all_sprites.has(self.player):
            #     self.player= Player()
            #     self.all_sprites.append(self.player)
            #     print("Spawned player?")
            # Limit to 60 fps
            clock= pygame.time.Clock()
            clock.tick(FPS)
            pygame.display.flip()
            #  blit the screen?

    def battle(self):
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(battleMusic)
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type== pygame.KEYDOWN:
                    # Key press event. Use this for pause later? Esc will also exit the game until we got a pause menu.
                    # print("Detected key press.")
                    if event.key == pygame.K_ESCAPE:
                        end = True
                        pygame.mixer.pause()
                        self.run()



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

    while not done and not game.battling:
        game.game_intro(screen)
#        game.new()
#        game.run()

    # If done, quit.
    pygame.quit()

if __name__ == "__main__":
    main()
