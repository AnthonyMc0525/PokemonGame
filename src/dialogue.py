import pygame
from strings import *

class Dialogue():
    def __init__(self, game):
        self.game= game


    def dialogue (self, dial):
        screen= self.game.screen
        self.dial= dial
        blackBarRectPos = (5, screen.get_width()-110) # For now.
        blackBarRectSize= (screen.get_width()-10, 100)
        pygame.draw.rect(screen, BLACK, pygame.Rect(blackBarRectPos, blackBarRectSize))
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(self.dial, True, WHITE, BLACK)
        textRect = text.get_rect()
        X = screen.get_width()
        Y = screen.get_height() + 375
        textRect.center = (X // 2, Y // 2)
        screen.blit(text, textRect)
