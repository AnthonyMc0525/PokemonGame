import sys
from os import path
import pygame
from random import randint

from pokemon import blastoise, blaziken, charizard, empoleon, feraligatr, infernape, meganium, sceptile, swampert, torterra, typhlosion, venusaur
from pokemon.pokemonTemplate import PokemonTemplate
from moves.grass import grassTemplate, magicalLeaf, petalBlizzard, petalDance, razorLeaf, seedBomb, solarBeam, vineWhip
from moves.fire import fireTemplate, burnUp, ember, Eruption, fireFang, fireSpin, flameCharge, flamethrower, flameWheel, flareBlitz, inferno, lavaPlume 
from moves.water import aquaTail, bubble, hydroPump, waterGun, waterPulse
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
        self.font= pygame.font.Font('freesansbold.ttf', 16)
        # Remove later
        #self.player_poke.append(charizard.Charizard())
        #self.enemy_poke.append(meganium.Meganium())
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def chooseMoves(self, pokemon, pokeType1, pokeType2="none"):
        randMoves = []
        names = []
        while len(randMoves) < 4:
            if pokeType1 == "grass":
                rand = randint(0, 6)
                if rand == 0:
                    ml = magicalLeaf.MagicalLeaf()
                    if ml.name in names:
                        continue
                    else:
                        names.append(ml.name)
                        randMoves.append(ml);
                elif rand == 1:
                    pb = petalBlizzard.PetalBlizzard()
                    if pb.name in names:
                        continue
                    else:
                        names.append(pb.name)
                        randMoves.append(pb);
                elif rand == 2:
                    pd = petalDance.PetalDance()
                    if pd.name in names:
                        continue
                    else:
                        names.append(pd.name)
                        randMoves.append(pd);
                elif rand == 3:
                    rl = razorLeaf.RazorLeaf()
                    if rl.name in names:
                        continue
                    else:
                        names.append(rl.name)
                        randMoves.append(rl);
                elif rand == 4:
                    sb = seedBomb.SeedBomb()
                    if sb.name in names:
                        continue
                    else:
                        names.append(sb.name)
                        randMoves.append(sb);
                elif rand == 5:
                    sB = solarBeam.SolarBeam()
                    if sB.name in names:
                        continue
                    else:
                        names.append(sB.name)
                        randMoves.append(sB);
                elif rand == 6:
                    vw = vineWhip.VineWhip()
                    if vw.name in names:
                        continue
                    else:
                        names.append(vw.name)
                        randMoves.append(vw);
            if pokeType1 == "fire":
                rand = randint(0, 10)
                if rand == 0:
                    bu = burnUp.BurnUp() 
                    if bu.name in names:
                        continue
                    else:
                        names.append(bu.name)
                        randMoves.append(bu);
                elif rand == 1:
                    e = ember.Ember()
                    if e.name in names:
                        continue
                    else:
                        names.append(e.name)
                        randMoves.append(e);
                elif rand == 2:
                    E = Eruption.Eruption()
                    if E.name in names:
                        continue
                    else:
                        names.append(E.name)
                        randMoves.append(E);
                elif rand == 3:
                    ff = fireFang.FireFang()
                    if ff.name in names:
                        continue
                    else:
                        names.append(ff.name)
                        randMoves.append(ff);
                elif rand == 4:
                    fs = fireSpin.FireSpin()
                    if fs.name in names:
                        continue
                    else:
                        names.append(fs.name)
                        randMoves.append(fs);
                elif rand == 5:
                    fc = flameCharge.FlameCharge()
                    if fc.name in names:
                        continue
                    else:
                        names.append(fc.name)
                        randMoves.append(fc);
                elif rand == 6:
                    ft = flamethrower.Flamethrower()
                    if ft.name in names:
                        continue
                    else:
                        names.append(ft.name)
                        randMoves.append(ft);
                elif rand == 7:
                    fw = flameWheel.FlameWheel()
                    if fw.name in names:
                        continue
                    else:
                        names.append(fw.name)
                        randMoves.append(fw);
                elif rand == 8:
                    fb = flareBlitz.FlareBlitz()
                    if fb.name in names:
                        continue
                    else:
                        names.append(fb.name)
                        randMoves.append(fb);
                elif rand == 9:
                    inf = inferno.Inferno()
                    if inf.name in names:
                        continue
                    else:
                        names.append(inf.name)
                        randMoves.append(inf);
                elif rand == 10:
                    lp = lavaPlume.LavaPlume()
                    if lp.name in names:
                        continue
                    else:
                        names.append(lp.name)
                        randMoves.append(lp);
            if pokeType1 == "water":
                rand = randint(0, 4)
                if rand == 0:
                    aq = aquaTail.AquaTail()
                    if aq.name in names:
                        continue
                    else:
                        names.append(aq.name)
                        randMoves.append(aq);
                elif rand == 1:
                    b = bubble.Bubble()
                    if b.name in names:
                        continue
                    else:
                        names.append(b.name)
                        randMoves.append(b);
                elif rand == 2:
                    hp = hydroPump.HydroPump()
                    if hp.name in names:
                        continue
                    else:
                        names.append(hp.name)
                        randMoves.append(hp);
                elif rand == 3:
                    wg = waterGun.WaterGun()
                    if wg.name in names:
                        continue
                    else:
                        names.append(wg.name)
                        randMoves.append(wg);
                elif rand == 4:
                    wp = waterPulse.WaterPulse()
                    if wp.name in names:
                        continue
                    else:
                        names.append(wp.name)
                        randMoves.append(wp);
                
        pokemon.moves = randMoves
        print(names)
        return rand

    def quit(self):
        pygame.mixer.pause()
        pygame.quit()
        sys.exit()

    def draw(self, screen):
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
        textRect_p = text_p.get_rect()
        textRect_p_name = text_p_name.get_rect()
        textRect_e = text_e.get_rect()
        textRect_e_name = text_e_name.get_rect()
        X_p = 50
        X_e = 500
        Y = screen.get_height()
        textRect_p.center = (X_p, Y // 2 - 200)
        textRect_p_name.center = (X_p, Y // 2 - 250)
        textRect_e.center = (X_e, Y // 2 - 200)
        textRect_e_name.center = (X_e, Y // 2 - 250)
        screen.blit(text_p, textRect_p)
        screen.blit(text_p_name, textRect_p_name)
        screen.blit(text_e, textRect_e)
        screen.blit(text_e_name, textRect_e_name)

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
            self.chooseMoves(rand_pokemon, "water")
        elif num == 1:
            rand_pokemon = blaziken.Blaziken()
            self.chooseMoves(rand_pokemon, "fire", )
        elif num == 2:
            rand_pokemon = charizard.Charizard()
            self.chooseMoves(rand_pokemon, "fire")
        elif num == 3:
            rand_pokemon = empoleon.Empoleon()
            self.chooseMoves(rand_pokemon, "water")
        elif num == 4:
            rand_pokemon = feraligatr.Feraligatr()
            self.chooseMoves(rand_pokemon, "water")
        elif num == 5:
            rand_pokemon = infernape.Infernape()
            self.chooseMoves(rand_pokemon, "fire")
        elif num == 6:
            rand_pokemon = meganium.Meganium()
            self.chooseMoves(rand_pokemon, "grass")
        elif num == 7:
            rand_pokemon = sceptile.Sceptile()
            self.chooseMoves(rand_pokemon, "grass")
        elif num == 8:
            rand_pokemon = swampert.Swampert()
            self.chooseMoves(rand_pokemon, "water")
        elif num == 9:
            rand_pokemon = torterra.Torterra()
            self.chooseMoves(rand_pokemon, "grass")
        elif num == 10:
            rand_pokemon = typhlosion.Typhlosion()
            self.chooseMoves(rand_pokemon, "fire")
        elif num == 11:
            # rand_pokemon = venusaur.Venusaur()
            rand_pokemon = typhlosion.Typhlosion()
            self.chooseMoves(rand_pokemon, "fire")

        return rand_pokemon

    def battle(self): #self, player, enemy
        p = randint(0, 11)
        e = randint(0, 11)
        pokeP = self.getPokemon(p)
        pokeE = self.getPokemon(e)

        self.player_poke.append(pokeP)
        self.enemy_poke.append(pokeE)

    def main(self):
        self.battle()
        print(self.player_poke[0].moves)
        print(self.enemy_poke[0].moves)
        self.game.battling=True
        size= [self.game.width,self.game.height]
        screen= pygame.display.set_mode(size)
        screen.fill(BLACK)
        game_folder = path.dirname(__file__)[0:-3]

        pp_name= self.player_poke[0].name
        pe_name= self.enemy_poke[0].name

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_name.lower() +'.png')).convert_alpha()
        play_poke= pygame.transform.flip(play_poke, True, False)
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_name.lower() +'.png')).convert_alpha()


        screen.blit(play_poke, (50, 100))
        screen.blit(enemy_poke, (380, 100))


        pygame.mixer.music.pause()
        # pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.draw(screen)
            self.events()
            pygame.display.flip()

        #  Make own events loop?
