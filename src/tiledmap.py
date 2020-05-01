import pygame as pg
import pytmx
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
def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)
class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "collision":
                    for obj in layer:
                        if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(block.rect) == True:
                            print("Collide!")
                            break

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
