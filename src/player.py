# import sys
# from os import path
# # ---- #
#
# import pygame as pygame
# from pygame.locals import *
# import pytmx
# import cv2
# import numpy as np
#
# # --- #
#
# from strings import *
#
# # --- #
#
# class Player(pygame.sprite.Sprite):
#     """
#     Spawn a player.
#     """
#
#     def __init__ (self, x=5, y=5):
#         pygame.sprite.Sprite.__init__(self)
#         self.images=[]
#         game_folder = path.dirname(__file__)[0:-3]
#         img= pygame.image.load(path.join(game_folder, 'assets/images/trainer_m.png')).convert()
#         self.images.append(img)
#         self.image = self.images[0]
#         self.rect = self.image.get_rect()
#         self.x=5
#         self.y=5
