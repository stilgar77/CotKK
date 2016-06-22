import time
import math

from artwork import Artwork 
import game_functions as gf

art3 = Artwork()

def spellBook(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print "spell book"
    print ""
    print "(H)eal"
    print "(L)ightening"
    print "(C)urse"
    print ""
    action = raw_input('>')
    if action in ['h', 'H']:
        heal(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['l', 'L']:
        lightening(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['c', 'C']:
        curse(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        

def heal(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if heal_used == 0:
        heal_used = 1
        time.sleep(1)
        print ""
        print "As you begin to cast, words of power fill your mind.  You concentrate on this litany of healing..."
        time.sleep(3)
        litany = 'My body is a broken vessel that is restored and filled by the healing light of the one source.'
        print ""
        print litany
        print ""
        print "This litany of healing begs to be said aloud..."
        time.sleep(2)
        print ""
        x = time.time()
        user_litany = raw_input('You say...')
        y = time.time()
        z = y - x
        time_taken = math.ceil(z)
        print ""
        heal_value = 25 - time_taken
        if user_litany == litany:
            heroHP = heroHP + heal_value
            print "You have been healed for", heal_value,"points of health!"
            gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        else:
            print "The spell has fizzled."
            gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        print "The page in your spellbook is blank."
        gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        

def lightening(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if lightening_used == 0:
        lightening_used = 1
        print "You focus your mind in order to atune your body to the electrical field of the planet."
        print "Electrical enery flows through you as you become the ultimate conductor!"
        art3.lightening();
    else:
        print "This page is blank in your spell book."
    gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);


def curse(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if curse_used == 0:
        curse_used = 1
        print "curse"
    else:
        print "This page is blank in your spell book."
    gf.combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
