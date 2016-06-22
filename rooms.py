import game_functions as gf
from artwork import Artwork

art2 = Artwork();

import time
import random

def room5(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if rm5_visited == 0:
        time.sleep(2)
        print "Here are your hero's stats:"
        time.sleep(1)
        print "HP =", heroHP
        time.sleep(1)
        print "AC =", heroAC
        time.sleep(1)
        print ""
        print "***Ability Scores***"
        time.sleep(1)
        print "STR =", heroSTR
        print "DEX =", heroDEX
        print "CON =", heroCON
        print "INT =", heroINT
        print "WIS =", heroWIS
        print "CHA =", heroCHA
        time.sleep(2)
        print ""
        print "Chamber one..."
        time.sleep(2)
        print ""
        print "After days of difficult travel, you stand before the opening of a foul cavern. The smell of rot wafts up from the darkness below."
        print "Rocks have been piled up in attempt to camoflage the entrance.  The promise of glory and treasure entices you forward."
        time.sleep(4)
        print ""
        print ""
        print "********************************************************************************************"
        print ""
        print "The way continues to the south.  (S)neak over the rocks and down into the cavern. (DEX check)"
        print ""
        print "(P)roceed south and smash the wall...the time for battle has come! (STR check)"
        print ""
        print "********************************************************************************************"
        print ""
        rm5_visited = rm5_visited + 1
        action = raw_input ('What would you like to do? (S or P) >')
        if action in ['s', 'S']:
            time.sleep(2)
            print ""
            print "You attempt to sneak into the cavern entrance."
            print ""
            time.sleep(2)
            die_roll = random.randint(1, 20)
            if die_roll <= heroDEX:
                print "Success!  You move quietly into the cavern and take a",encounter_monsterName,"by suprise."
                print ""
                time.sleep(2)
                art2.showKobold();
                time.sleep(1)
                gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
            else:
                time.sleep(2)
                print "You stumble!"
                time.sleep(1)
                print ""
                print "You catch your cloak on a rock and set the rocks tumbling!  You've alerted the guard..."
                gf.monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        if action in ['p', 'P']:
            time.sleep(2)
            print ""
            print "You charge forward slamming into the rocks..."
            print ""
            die_roll = random.randint(1, 20)
            if die_roll <= heroSTR:
                time.sleep(2)
                print "...and bust through taking a",encounter_monsterName,"by suprise!"
                time.sleep(1)
                print ""
                art2.showKobold();
                gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
            else:
                time.sleep(2)
                print "...and slam into a solid wall of stone!  You have alerted the guard!"
                art2.showKobold();
                gf.monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        print "You have been here before. Some light filters down from the surface and a kobold is dead on the floor."
        gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    
def room15(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if rm15_visited == 0:
        art2.chamber2();
        print ""
        print "The cavern entrance opens up to a chamber choked with spider webs.  Cutting and pushing them aside the best you can, you move into the room."
        print "You are certain that something dangerous is living here.  You stop to consider your next move."
        print ""
        print "********************************************************************************************"
        print ""
        print "Light a torch and (b)urn the webs to clear a path. (INT check)"
        print ""
        print "(M)ove quietly and carefully through the webs to avoid disturbing any potential arachnid inhabitants. (DEX check)"
        print ""
        print "********************************************************************************************"
        print ""
        action = raw_input ('What would you like to do? (B or M) >')
        rm15_visited = rm15_visited + 1
        if action in ['b', 'B']:
            time.sleep(1)
            print ""
            print "You take a torch from your pack, set it alight and touch it to the webs..."
            print ""
            time.sleep(2)
            die_roll = random.randint(1, 20)
            if die_roll <= heroINT:
                print "Success!  The webs catch fire and the room erupts in flames!"
                art2.flames();
                print ""
                print "You hear the chittering scream of hundreds of burning spiders."
                art2.spiders();
            else:
                time.sleep(2)
                print ""
                print "You light a torch and start to hold it to the webs. Casting the dark aside reveals the hundreds of eyes and snapping mandibles of a huge spider!"
                print ""
                art2.showSpider();
                time.sleep(2)
                gf.monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
                
            
            
            
        
        
     
    gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def room25(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print "room25"
    gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def room24(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print "room24"
    gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def room34(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print "room34"
    gf.nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);



    
