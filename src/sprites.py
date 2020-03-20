# Sprite classes
import sys

import pygame as pygame
from os import path

from strings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((16,32), pygame.SRCALPHA)
        self.image.fill(BLACK)
        self.image.set_alpha(128)
        self.images=[]
        game_folder = path.dirname(__file__)[0:-3]
        self.images.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_m.png')).convert_alpha()) # 0
        self.images.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_m2.png')).convert_alpha()) # 1
        self.images.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_m.png')).convert_alpha()) # 2
        self.images.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_m3.png')).convert_alpha()) # 3
        # Where we are in the sprite.
        self.index= 0
        self.image = self.images[self.index]
        self.rect= self.image.get_rect()
        self.vx=23 *16
        self.vy=9 *16
        self.speed=4

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # self.vx=0
        keys= pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                # print("AAAA")
                self.index+= 1
                if self.index >= len(self.images):
                    self.index=0
                self.image=self.images[self.index]
                if event.key== pygame.K_LEFT:
                    self.vx -= self.speed
                elif event.key == pygame.K_RIGHT:
                    self.vx += self.speed
                elif event.key == pygame.K_UP:
                    self.vy -= self.speed
                elif event.key == pygame.K_DOWN:
                    self.vy += self.speed
            elif event.type == pygame.KEYUP:
                self.index=0
                self.image= self.images[self.index]
            elif event.type== pygame.QUIT:
                self.quit()
            # if keys[pygame.K_LEFT]:
            #     self.vx = -5
            # if keys[pygame.K_RIGHT]:
            #     self.vx = 5

        self.rect.x += self.vx
        self.rect.y += self.vy
