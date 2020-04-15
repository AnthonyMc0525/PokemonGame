import sys
from os import path

import pygame

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

    def main():
        size= [game.width,game.height]
        screen= pygame.display.set_mode(size)
        screen.fill(BLACK)
        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ self.player_poke[0] +'.png')).convert_alpha()
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ self.enemy_poke[0] +'.png')).convert_alpha()
        play_rect= play_poke.get_rect()
        ene_rect= enemy_poke.get_rect()

        screen.blit(play_poke, play_rect)
        screen.blit(play_poke, ene_rect)
        pygame.display.flip()
        pygame.mixer.Sound("sounds/battle.wav")
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(battleMusic)
