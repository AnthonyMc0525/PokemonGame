import sys
from os import path
# ---- #
import pygame
import pytmx
# import cv2
# ---- #

class TiledMap:
    """
    Loads and renders Tiled maps.
    """
    def __init__(self, filename):
        tm= pytmx.load_pygame(filename, pixelalpha= True)
        # Width/Height is how many tiles the map is. The tilewidth/tileheight property is how many pixels the tiles are (Should always be 16 but just in case...)
        self.width= tm.width * tm.tilewidth
        self.height= tm.height * tm.tileheight
        self.tmxdata= tm

    def render(self, surface):
        ti= self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                # We need co-ords and IDs.
                for x, y, gid, in layer:
                    tile= ti(gid)
                    if tile:
                        map_x= x * self.tmxdata.tilewidth
                        map_y= y * self.tmxdata.tileheight
                        surface.blit(tile, (map_x, map_y))
                        # self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

    def make_map(self):
        temp_surface= pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
