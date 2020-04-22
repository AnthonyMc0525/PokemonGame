import sys
from os import path
import pygame
from random import randint

from pokemon import blastoise, blaziken, charizard, empoleon, feraligatr, infernape, meganium, sceptile, swampert, torterra, typhlosion, venusaur
from pokemon.pokemonTemplate import PokemonTemplate
from moves.grass import grassTemplate, magicalLeaf, petalBlizzard, petalDance, razorLeaf, seedBomb, solarBeam, vineWhip
from strings import *
from dialogue import *


class Battle():
    def __init__(self, game):
        pygame.mixer.init()
        self.turns=0
        self.player_poke=[]
        self.enemy_poke=[]
        self.won= None # Not True not False it's just ¯\_(ツ)_/¯
        self.done= False
        self.game= game
        self.player_move_names=[]
        self.font= pygame.font.Font('freesansbold.ttf', 16)
        self.big_font= pygame.font.Font('freesansbold.ttf', 24)
        # Remove later
        #self.player_poke.append(charizard.Charizard())
        #self.enemy_poke.append(meganium.Meganium())
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def chooseMoves(self, pokeType, pokemon):
        randMoves = []
        while len(randMoves) < 4:
            if pokeType == "grass":
                rand = randint(0, 6)
                if rand == 0:
                    ml = magicalLeaf.MagicalLeaf()
                    randMoves.append(ml);
                elif rand == 1:
                    pb = petalBlizzard.PetalBlizzard()
                    randMoves.append(pb);
                elif rand == 2:
                    pd = petalDance.PetalDance()
                    randMoves.append(pd);
                elif rand == 3:
                    rl = razorLeaf.RazorLeaf()
                    randMoves.append(rl);
                elif rand == 4:
                    sb = seedBomb.SeedBomb()
                    randMoves.append(sb);
                elif rand == 5:
                    sB = solarBeam.SolarBeam()
                    randMoves.append(sB);
                elif rand == 6:
                    vw = vineWhip.VineWhip()
                    randMoves.append(vw);

        pokemon.moves = randMoves


        return rand

    def quit(self):
        pygame.mixer.pause()
        pygame.quit()
        sys.exit()

    def draw(self, screen):
        screen.fill(BLACK)
        game_folder = path.dirname(__file__)[0:-3]

        pp_name= self.player_poke[0].name
        pe_name= self.enemy_poke[0].name

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_name.lower() +'.png')).convert_alpha()
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_name.lower() +'.png')).convert_alpha()
        enemy_poke= pygame.transform.flip(enemy_poke, True, False)
        platform_img= pygame.image.load(path.join(game_folder, 'assets/images/platform.png')).convert_alpha()
        platform_img_ene= pygame.image.load(path.join(game_folder, 'assets/images/platform.png')).convert_alpha()
        platform_img_ene= pygame.transform.flip(platform_img_ene, True, False)
        spotlight_img= pygame.image.load(path.join(game_folder, 'assets/images/spotlight.png')).convert_alpha()

        screen.blit(spotlight_img, (100, 0))
        screen.blit(platform_img, (50, 115))
        screen.blit(play_poke, (50, 100))
        screen.blit(spotlight_img, (350, 0))
        screen.blit(platform_img_ene, (380, 115))
        screen.blit(enemy_poke, (380, 100))


        self.enemy_poke[0].currentHp= self.enemy_poke[0].stats['hp']
        self.player_poke[0].currentHp= self.player_poke[0].stats['hp']
        player_name= str(self.player_poke[0].name).capitalize()
        enemy_name= str(self.enemy_poke[0].name).capitalize()
        player_hp= str(self.player_poke[0].currentHp) + "/" + str(self.player_poke[0].stats['hp'])
        enemy_hp= str(self.enemy_poke[0].currentHp) + "/" + str(self.enemy_poke[0].stats['hp'])
        text_p = self.font.render(player_hp, True, WHITE, BLACK)
        text_p_name = self.font.render(player_name, True, WHITE, BLACK)
        text_e = self.font.render(enemy_hp, True, WHITE, BLACK)
        text_e_name = self.font.render(enemy_name, True, WHITE, BLACK)
        prompt = self.font.render(BATTLE_PROMPT.replace("you", player_name), True, WHITE, BLACK)
        textRect_p = text_p.get_rect()
        textRect_p_name = text_p_name.get_rect()
        textRect_e = text_e.get_rect()
        textRect_e_name = text_e_name.get_rect()
        textRect_prompt= prompt.get_rect()
        X_p = 50
        X_e = 500
        X = screen.get_width()
        Y = screen.get_height()
        textRect_p.center = (X_p, Y // 2 - 200)
        textRect_p_name.center = (X_p, Y // 2 - 250)
        textRect_e.center = (X_e, Y // 2 - 200)
        textRect_e_name.center = (X_e, Y // 2 - 250)
        textRect_prompt.center= (X//2, Y//2)
        screen.blit(text_p, textRect_p)
        screen.blit(text_p_name, textRect_p_name)
        screen.blit(text_e, textRect_e)
        screen.blit(text_e_name, textRect_e_name)
        # pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        pygame.draw.rect(screen, RED, (25, 300, 200, 100 ))
        pygame.draw.rect(screen, RED, (25, 425, 200, 100 ))
        pygame.draw.rect(screen, RED, (325, 300, 200, 100 ))
        pygame.draw.rect(screen, RED, (325, 425, 200, 100 ))
        screen.blit(prompt, textRect_prompt)
        try:
            move1= str(self.player_move_names[0]).capitalize()
            move2= str(self.player_move_names[1]).capitalize()
            move3=str(self.player_move_names[2]).capitalize()
            move4= str(self.player_move_names[3]).capitalize()
            text_m1 = self.big_font.render(move1, True, WHITE, RED)
            text_m2 = self.big_font.render(move2, True, WHITE, RED)
            text_m3 = self.big_font.render(move3, True, WHITE, RED)
            text_m4 = self.big_font.render(move4, True, WHITE, RED)
            textRect_m1 = text_m1.get_rect()
            textRect_m2 = text_m2.get_rect()
            textRect_m3 = text_m3.get_rect()
            textRect_m4 = text_m4.get_rect()
            textRect_m1.center= (120, 350)
            textRect_m2.center= (425, 350)
            textRect_m3.center= (120, 475)
            textRect_m4.center= (425, 475)
            screen.blit(text_m1, textRect_m1)
            screen.blit(text_m2, textRect_m2)
            screen.blit(text_m3, textRect_m3)
            screen.blit(text_m4, textRect_m4)
        except:
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
            self.chooseMoves("grass", rand_pokemon)
        elif num == 7:
            rand_pokemon = sceptile.Sceptile()
            self.chooseMoves("grass", rand_pokemon)
        elif num == 8:
            rand_pokemon = swampert.Swampert()
        elif num == 9:
            rand_pokemon = torterra.Torterra()
            self.chooseMoves("grass", rand_pokemon)
        elif num == 10:
            rand_pokemon = typhlosion.Typhlosion()
        elif num == 11:
            # rand_pokemon = venusaur.Venusaur()
            rand_pokemon = typhlosion.Typhlosion()

        return rand_pokemon

    def battle(self): #self, player, enemy
        p = randint(0, 11)
        e = randint(0, 11)
        pokeP = self.getPokemon(p)
        pokeE = self.getPokemon(e)

        self.player_poke.append(pokeP)
        self.enemy_poke.append(pokeE)

    def main(self):
        size= [self.game.width,self.game.height]
        screen= pygame.display.set_mode(size)
        self.battle()
        print(self.player_poke[0].moves)
        for item in self.player_poke[0].moves:
            self.player_move_names.append(item.name)
            print(item.name)
        self.game.battling=True



        pygame.mixer.music.pause()
        # pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.draw(screen)
            self.events()
            pygame.display.flip()

        #  Make own events loop?
