import pygame
from os import path
game_folder = path.dirname(__file__)[0:-3]

from strings import *

size= [700,700]
screen= pygame.display.set_mode(size)

default_sprite= pygame.image.load(path.join(game_folder, 'assets/images/trainer_f.png')).convert_alpha()
class NpcTemplate(pygame.sprite.Sprite):
    def __init__(self, game, x, y, name, sprite=default_sprite, dialog='Hello'):
        self.name = name
        self.game=game
        self.vx=x
        self.vy= y
        self.image= pygame.Surface((16,32), pygame.SRCALPHA)
        self.sprite = sprite
        self.rect= self.image.get_rect()
        self.dialog = dialog
        self.font = pygame.font.SysFont(None, 25)
        default_sprite= pygame.image.load(path.join(game_folder, 'assets/images/'+ self.name+'_npc.png')).convert_alpha()
        self.image= default_sprite

        # self.game.npcs

    def runDialog(self, screen):
        done = False
        while not done:
            for i, line in enumerate(dialog):
                #display to the player the dialog
                screen_text = font.render(line, True, (255, 255, 255))
                pygame.draw.rect(screen, (0, 0, 0), [100, 100, 100, 200])
                screen.blit(screen_text, [100, 100])
                for e in pygame.even.get():
                    #if player clicks screen display next option or breakout of loop
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if dialog[i] == dialog.length - 1:
                            done = True
                            break
                        else:
                            continue

    # def giveItem(self, player):
    #     if self.item != None:
    #         if self.item.name in player.inventory:
    #             for key, value in player.inventory.items()
    #                 if key == self.item.name:
    #                     player.inventory[key] = value + 1
    #         else:
    #             player.inventory[self.item.name] = 1
