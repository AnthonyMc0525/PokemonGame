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
        self.button_list=[1, 2, 3, 4]
        self.button_no= self.button_list[0]
        self.player_move_names=[]
        self.font= pygame.font.Font('freesansbold.ttf', 16)
        self.big_font= pygame.font.Font('freesansbold.ttf', 24)
        # Remove later
        #self.player_poke.append(charizard.Charizard())
        #self.enemy_poke.append(meganium.Meganium())
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def chooseMoves(self, pokemon, pokeType1, pokeType2="none"):
        randMoves = []
        names = []
        while len(randMoves) < 4:
            if pokeType1 == "grass" and pokeType2 == "none":
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
            if pokeType1 == "fire" and pokeType2 == "none":
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
            if pokeType1 == "water" and pokeType == "none":
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
        screen.fill(ALMOST_BLACK)
        game_folder = path.dirname(__file__)[0:-3]

        pp_name= self.player_poke[0].name
        pe_name= self.enemy_poke[0].name
        pp_type= self.player_poke[0].type
        pe_type= self.enemy_poke[0].type

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_name.lower() +'.png')).convert_alpha()
        play_type=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_type.lower() +'.png')).convert_alpha()
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_name.lower() +'.png')).convert_alpha()
        enemy_type=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_type.lower() +'.png')).convert_alpha()
        enemy_poke= pygame.transform.flip(enemy_poke, True, False)
        platform_img= pygame.image.load(path.join(game_folder, 'assets/images/platform.png')).convert_alpha()
        platform_img_ene= pygame.image.load(path.join(game_folder, 'assets/images/platform.png')).convert_alpha()
        platform_img_ene= pygame.transform.flip(platform_img_ene, True, False)
        spotlight_img= pygame.image.load(path.join(game_folder, 'assets/images/spotlight.png')).convert_alpha()


        spotlight_size = spotlight_img.get_size()
        spotlight_img = pygame.transform.scale(spotlight_img, (int(spotlight_size[0]), int(spotlight_size[1]*2)))

        screen.blit(spotlight_img, (100, 0))
        screen.blit(platform_img, (50, 115))
        screen.blit(play_poke, (50, 100))
        screen.blit(spotlight_img, (350, 0))
        screen.blit(platform_img_ene, (380, 115))
        screen.blit(enemy_poke, (380, 100))
        screen.blit(play_type, (30, 100))
        screen.blit(enemy_type, (490, 100))


        self.enemy_poke[0].currentHp= self.enemy_poke[0].stats['hp']
        self.player_poke[0].currentHp= self.player_poke[0].stats['hp']
        player_name= str(self.player_poke[0].name).capitalize()
        enemy_name= str(self.enemy_poke[0].name).capitalize()
        player_hp= str(self.player_poke[0].currentHp) + "/" + str(self.player_poke[0].stats['hp'])
        enemy_hp= str(self.enemy_poke[0].currentHp) + "/" + str(self.enemy_poke[0].stats['hp'])
        text_p = self.font.render(player_hp, True, WHITE)
        text_p_name = self.font.render(player_name, True, WHITE)
        text_e = self.font.render(enemy_hp, True, WHITE)
        text_e_name = self.font.render(enemy_name, True, WHITE)
        prompt = self.font.render(BATTLE_PROMPT.replace("you", player_name), True, WHITE)
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
        # This will get nasty but oh well...
        if self.button_no == 1:
            pygame.draw.rect(screen, SELECTED_BTN, (25, 300, 200, 100 ))
        else:
            pygame.draw.rect(screen, BTN_COLOUR, (25, 300, 200, 100 ))
        if self.button_no == 2:
            pygame.draw.rect(screen, SELECTED_BTN, (25, 425, 200, 100 ))
        else:
            pygame.draw.rect(screen, BTN_COLOUR, (25, 425, 200, 100 ))
        if self.button_no== 3:
            pygame.draw.rect(screen, SELECTED_BTN, (325, 300, 200, 100 ))
        else:
            pygame.draw.rect(screen, BTN_COLOUR, (325, 300, 200, 100 ))
        if self.button_no == 4:
            pygame.draw.rect(screen, SELECTED_BTN, (325, 425, 200, 100 ))
        else:
            pygame.draw.rect(screen, BTN_COLOUR, (325, 425, 200, 100 ))
        # ------ #

        screen.blit(prompt, textRect_prompt)
        try:
            move1= str(self.player_move_names[0]).capitalize()
            move3= str(self.player_move_names[1]).capitalize()
            move2= str(self.player_move_names[2]).capitalize()
            move4= str(self.player_move_names[3]).capitalize()
            text_m1 = self.big_font.render(move1, True, WHITE)
            text_m2 = self.big_font.render(move2, True, WHITE)
            text_m3 = self.big_font.render(move3, True, WHITE)
            text_m4 = self.big_font.render(move4, True, WHITE)
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
                    elif event.key == pygame.K_DOWN:
                        if self.button_no == 2:
                            self.button_no = 1
                        elif self.button_no == 4:
                            self.button_no = 3
                        elif self.button_no == 1:
                            self.button_no= 2
                        else:
                            # Number is 3
                            self.button_no = 4
                    elif event.key == pygame.K_UP:
                        if self.button_no == 2:
                            self.button_no = 1
                        elif self.button_no == 4:
                            self.button_no = 3
                        elif self.button_no== 1:
                            self.button_no= 2
                        else:
                            self.button_no= 4
                    elif event.key == pygame.K_LEFT:
                        if self.button_no == 3:
                            self.button_no = 1
                        elif self.button_no == 4:
                            self.button_no = 2
                        elif self.button_no== 1:
                            self.button_no= 3
                        else:
                            self.button_no= 4
                    elif event.key == pygame.K_RIGHT:
                        if self.button_no == 1:
                            self.button_no = 3
                        elif self.button_no == 2:
                            self.button_no = 4
                        elif self.button_no == 3:
                            self.button_no = 1
                        else:
                            self.button_no= 2
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        move_name= self.player_poke[0].moves[self.button_no-1].name
                        print("Pokemon used " + move_name +"!")

    def getPokemon(self, num):
        rand_pokemon = 0
        if num == 0:
            rand_pokemon = blastoise.Blastoise()
            self.chooseMoves(rand_pokemon, "water")
        elif num == 1:
            rand_pokemon = blaziken.Blaziken()
            self.chooseMoves(rand_pokemon, "fire" )
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
            rand_pokemon = venusaur.Venusaur()
            self.chooseMoves(rand_pokemon, "grass")

        print (rand_pokemon.name)
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
