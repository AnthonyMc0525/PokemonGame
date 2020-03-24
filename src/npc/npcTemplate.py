import pygame

class NpcTemplate():
    def __init__(self, name, sprite, dialog, item):
        self.name = name
        self.sprite = sprite
        self.dialog = dialog
        self.item = item
        self.font = pygame.font.SysFont(None, 25)

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

    def giveItem(self, player):
        if self.item != None:
            if self.item.name in player.inventory:
                for key, value in player.inventory.items()
                    if key == self.item.name:
                        player.inventory[key] = value + 1
            else:
                player.inventory[self.item.name] = 1

