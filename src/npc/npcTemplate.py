import pygame

class NpcTemplate():
    def __init__(self, name, sprite, dialog, npcType):
        self.name = name
        self.sprite = sprite
        self.dialog = dialog
        self.npcType = npcType #types will either be nonCombat or Combat depending if the npc is a trainer/elite four or just a normal npc
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
