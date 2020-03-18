# import sys
# from os import path
# # ---- #
# import pygame
# import pytmx
# # import cv2
# # ---- #
#
# from strings import *
#
# # ---- #
#
# class TiledMap:
#     """
#     Loads and renders Tiled maps.
#     """
#     def __init__(self, filename):
#         tm= pytmx.load_pygame(filename, pixelalpha= True)
#         # Width/Height is how many tiles the map is. The tilewidth/tileheight property is how many pixels the tiles are (Should always be 16 but just in case...)
#         self.width= tm.width * tm.tilewidth
#         self.height= tm.height * tm.tileheight
#         self.tmxdata= tm
#
#
#                         # self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
#
#     def make_map(self):
#         temp_surface= pygame.Surface((self.width, self.height))
#         self.render(temp_surface)
#         return temp_surface
