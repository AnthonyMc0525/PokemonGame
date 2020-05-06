# Sprite classes
import sys

import pygame as pygame
from os import path


from strings import *

class Teleport(pygame.sprite.Sprite):
    def __init__(self, game, x,y,w,h,map_name):
        pygame.sprite.Sprite.__init__(self)
        self.rect= pygame.Rect(x,y,w,h)
        self.map_name= map_name

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
        self.pos= pygame.math.Vector2(x,y)
        self.width= w
        self.height= h


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect= pygame.Rect(x,y,16,32)
        self.vx=x
        self.vy=y
        self.rect.x= x
        self.rect.y= y
        self.image= pygame.Surface((16,32), pygame.SRCALPHA)
        self.image.fill(BLUE)
        self.image.set_alpha(128)
        self.imagesdown=[]
        self.imagesright=[]
        self.imagesleft=[]
        self.imagesup=[]
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
        # self.rect= self.image.get_rect()
        self.speed=4
        self.dir="up"

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self,event):
        # self.vx=0
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT or event.key== pygame.K_a:
                self.dir="left"
                self.vx -= self.speed
                self.rect.x -= self.speed
                self.index+= 1
                if self.index >= len(self.imagesleft):
                    self.index=0
                self.image= pygame.transform.flip(self.imagesleft[self.index], True, False)
            elif event.key == pygame.K_RIGHT or event.key== pygame.K_d:
                self.dir="right"
                self.vx += self.speed
                self.rect.x += self.speed
                self.index+= 1
                if self.index >= len(self.imagesright):
                    self.index=0
                self.image=self.imagesright[self.index]

            elif event.key == pygame.K_UP or event.key== pygame.K_w:
                self.dir="up"
                self.vy -= self.speed
                self.rect.y -= self.speed
                self.index+= 1
                if self.index >= len(self.imagesup):
                    self.index=0
                self.image=self.imagesup[self.index]
            elif event.key == pygame.K_DOWN or event.key== pygame.K_s:
                self.dir="down"
                self.vy += self.speed
                self.rect.y += self.speed
                self.index+= 1
                if self.index >= len(self.imagesdown):
                    self.index=0
                self.image=self.imagesdown[self.index]

        # elif event.type == pygame.KEYUP:
        #     self.index=0
        #     if self.dir=="down":
        #         self.image= self.imagesdown[self.index]
        #     elif self.dir=="right":
        #         self.image= self.imagesright[self.index]
        #     else:
        #         self.image= self.imagesdown[self.index]
        elif event.type== pygame.QUIT:
            self.quit()
