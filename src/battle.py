import sys
from os import path

import pygame

import main
import pokemon
from strings import *

class Battle():
    def __init__(self, game):
        pygame.mixer.init()
        self.turns=0
        self.player_poke=[]
        self.enemy_poke=[]
        self.won= None # Not True not False it's just ¯\_(ツ)_/¯
        self.done= False
        self.game= game
        # Remove later
        self.player_poke.append('charizard')
        self.enemy_poke.append('bulbasaur')
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def quit(self):
        pygame.mixer.pause()
        pygame.quit()
        sys.exit()

    def events(self):
        if self.game.battling== True:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    print("Bye bye...")
                    self.quit()
                elif event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        print("See ya.")
                        self.quit()
                    elif event.key== pygame.K_q:
                        print("Q key pressed.")
                        self.game.battling=False
                        self.done= True
                        pygame.mixer.Sound.fadeout(self.music,1000)
                        main.main()

    def main(self):
        self.game.battling=True
        size= [self.game.width,self.game.height]
        screen= pygame.display.set_mode(size)
        screen.fill(BLACK)
        game_folder = path.dirname(__file__)[0:-3]

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ self.player_poke[0] +'.png')).convert_alpha()
        play_poke= pygame.transform.flip(play_poke, True, False)
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ self.enemy_poke[0] +'.png')).convert_alpha()
        play_rect= play_poke.get_rect()
        ene_rect= enemy_poke.get_rect()

        screen.blit(play_poke, (50, 100))
        screen.blit(enemy_poke, (380, 100))
        pygame.display.flip()
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.events()

        #  Make own events loop?
