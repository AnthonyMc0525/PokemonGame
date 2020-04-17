import sys
from os import path

import pygame
from random import randint

import main
from pokemon import blastoise, blaziken, charizard, empoleon, feraligatr, infernape, meganium, sceptile, swampert, torterra, typhlosion, venusaur
from pokemon.pokemonTemplate import PokemonTemplate
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
#        self.player_poke.append('charizard')
#        self.enemy_poke.append('bulbasaur')
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

    def getPokemon(self, num):
        rand_pokemon = 0
        if num == 0:
            rand_pokemon = blastoise.Blastoise()
        elif num == 1:
            rand_pokemon = blaziken.Blaziken()
        elif num == 2:
            rand_pokemon = charizard.Charizard()
        elif num == 3:
            rand_pokemon = empoleon.Empoleon()
        elif num == 4:
            rand_pokemon = feraligatr.Feraligatr()
        elif num == 5:
            rand_pokemon = infernape.Infernape()
        elif num == 6:
            rand_pokemon = meganium.Meganium()
        elif num == 7:
            rand_pokemon = sceptile.Sceptile()
        elif num == 8:
            rand_pokemon = swampert.Swampert()
        elif num == 9:
            rand_pokemon = torterra.Torterra()
        elif num == 10:
            rand_pokemon = typhlosion.Typhlosion()
        elif num == 11:
            rand_pokemon = venusaur.Venusaur()

        return rand_pokemon

    def battle(self): #self, player, enemy
        p = randint(0, 11)
        e = randint(0, 11)
        
        pokeP = self.getPokemon(p)
        pokeE = self.getPokemon(e)
        

        self.player_poke.append(pokeP.name)
        self.enemy_poke.append(pokeE.name)


    def main(self):
        self.battle()
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
        self.battle()

        screen.blit(play_poke, (50, 100))
        screen.blit(enemy_poke, (380, 100))
        pygame.display.flip()
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.events()

        #  Make own events loop?
