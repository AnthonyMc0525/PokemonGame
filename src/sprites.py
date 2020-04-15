# Sprite classes
import sys

import pygame as pygame
from os import path

from strings import *

vector= pygame.math.Vector2

from tiledmap import collide_hit_rect


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x,y,w,h):
        self.walls = pg.sprite.Group()
        self.groups= self.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game= game
        self.rect= pygame.Rect(x,y,w,h)
        self.hit_rect= self.rect
        self.x= x
        self.y= y
        self.rect.x= x
        self.rect.y= y
        self.pos= vector(x,y)


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.hitbox=(x, y, 16, 32)
        self.image= pygame.Surface((16,32), pygame.SRCALPHA)
        self.image.fill(BLACK)
        self.image.set_alpha(128)
        self.imagesdown=[]
        self.game= game
        self.imagesright=[]
        self.imagesleft=[]
        self.imagesup=[]
        self.pos= vector(x,y)
        self.vel= vector(0,0)
        self.gender="m"
        game_folder = path.dirname(__file__)[0:-3]
        self.imagesdown.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_'+ self.gender +'.png')).convert_alpha()) # 0
        self.imagesdown.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender +'2.png')).convert_alpha()) # 1
        self.imagesdown.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender +'.png')).convert_alpha()) # 2
        self.imagesdown.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '3.png')).convert_alpha()) # 3
        # ---- #
        self.imagesright.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side.png')).convert_alpha()) # 0
        self.imagesright.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender +'_side2.png')).convert_alpha()) # 1
        self.imagesright.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender +'_side.png')).convert_alpha()) # 2
        self.imagesright.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side3.png')).convert_alpha()) # 3
        # ---- #
        self.imagesleft.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side.png')).convert_alpha()) # 0
        self.imagesleft.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side2.png')).convert_alpha()) # 1
        self.imagesleft.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side.png')).convert_alpha()) # 2
        self.imagesleft.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_side3.png')).convert_alpha()) # 3
        # ---- #
        self.imagesup.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_up.png')).convert_alpha()) # 0
        self.imagesup.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_up2.png')).convert_alpha()) # 1
        self.imagesup.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_up.png')).convert_alpha()) # 2
        self.imagesup.append(pygame.image.load(path.join(game_folder, 'assets/images/trainer_' + self.gender + '_up3.png')).convert_alpha()) # 3

        # Where we are in the sprite.
        self.index= 0
        self.image = self.imagesdown[self.index]
        self.rect= self.image.get_rect()
        self.vx=x
        self.vy=y
        self.speed=4
        self.dir="down"
        self.font = pygame.font.SysFont(None, 25)


    def quit(self):
        pygame.quit()
        sys.exit()


    def update(self, event):
        # self.vx=0
        if event.type== pygame.KEYDOWN:
                # Max right: 538
                # Max left: 3
                # Max up: -1
                # Max Down: 529

            if event.key== pygame.K_LEFT or event.key == pygame.K_a:
                if self.vx > MAX_LEFT and self.vx <= MAX_RIGHT:
                    self.dir="left"
                    self.vx -= self.speed
                    self.index+= 1
                    if self.index >= len(self.imagesleft):
                        self.index=0
                    self.image= pygame.transform.flip(self.imagesleft[self.index], True, False)

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if self.vx >= MAX_LEFT and self.vx < MAX_RIGHT:
                    self.dir="right"
                    self.vx += self.speed
                    self.index+= 1
                    if self.index >= len(self.imagesright):
                        self.index=0
                    self.image=self.imagesright[self.index]

            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if self.vy > MAX_UP and self.vy <= MAX_DOWN:
                    self.dir="up"
                    self.vy -= self.speed
                    self.index+= 1
                    if self.index >= len(self.imagesup):
                        self.index=0
                    self.image=self.imagesup[self.index]
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if self.vy >= MAX_UP and self.vy < MAX_DOWN:
                    self.dir="down"
                    self.vy += self.speed
                    self.index+= 1
                    if self.index >= len(self.imagesdown):
                        self.index=0
                    self.image=self.imagesdown[self.index]

            elif event.type== pygame.QUIT:
                self.quit()
            self.hitbox=(self.vx+20, self.vy, 16, 32)
            self.pos= vector(self.vx, self.vy)

        self.rect.x += self.vx
        self.rect.y += self.vy
