import sys
from os import path
import pygame
import random

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
        self.player_poke.append(charizard.Charizard())
        self.enemy_poke.append(meganium.Meganium())
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def quit(self):
        pygame.mixer.pause()
        pygame.quit()
        sys.exit()

    def draw(self):
        pass

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
                        self.game.run()

    def getPokemon(num):
        rand_pokemon = 0
        if num == 0:
            rand_pokemon = Blastoise()
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 7:
            pass
        elif num == 8:
            pass
        elif num == 9:
            pass
        elif num == 10:
            pass
        elif num == 11:
            pass

    def battle(self, player, enemy):
        p = randint(0, 11)
        e = randint(0, 11)

        player_pokemon = pokemon[p]
        enemy_pokemon = pokemon[e]
        self.player_poke.append(player_pokemon.name)
        self.enemy_poke.append(enemy_pokemon.name)


    def main(self):
        self.game.battling=True
        size= [self.game.width,self.game.height]
        screen= pygame.display.set_mode(size)
        screen.fill(BLACK)
        game_folder = path.dirname(__file__)[0:-3]
        print(self.player_poke[0].name)
        print(self.enemy_poke[0].name)

        pp_name= self.player_poke[0].name
        pe_name= self.enemy_poke[0].name

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_name.lower() +'.png')).convert_alpha()
        play_poke= pygame.transform.flip(play_poke, True, False)
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_name.lower() +'.png')).convert_alpha()


        screen.blit(play_poke, (50, 100))
        screen.blit(enemy_poke, (380, 100))

        self.battle(self.player_poke[0], self.enemy_poke[0])

        pygame.display.flip()
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.events()

        #  Make own events loop?
