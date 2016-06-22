from monster import Monster
import spellbook as sb
import random
import time
import sys

import rooms as r

valid_locations = [5, 15, 25, 24, 34]

m2 = Monster('spider', 8, 12, 2)
m3 = Monster('ogre', 14, 12, 2)
m4 = Monster('Kobold King', 18, 12, 2)
  

def nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    print "Your current location is", location
    print ""
    print "What would you like to do?"
    print ""
    print "Go (N)orth"
    print "Go (S)outh"
    print "Go (W)est"
    print "Go (E)ast"
    print ""
    print "(P)rint Stats"
    print ""
    action = raw_input('>')
    if action in ['n', 'N']:
        go_north(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['s', 'S']:
        go_south(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['w', 'W']:
        go_west(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['e', 'E']:
        go_east(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if action in ['p', 'P']:
        printStats(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def go_north(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    location = location + 10
    if location in valid_locations:
        room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        location = location - 10
        print "You can't go that way."
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def go_south(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    location = location - 10
    if location in valid_locations:
        room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        location = location + 10
        print "You can't go that way."
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def go_west(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    location = location - 1
    if location in valid_locations:
        room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        location = location + 1
        print "You can't go that way."
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    
        
def go_east(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    location = location + 1
    if location in valid_locations:
        room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        location = location - 1
        print "You can't go that way."
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    

def room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if location == 5:
        r.room5(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if location == 15:
        r.room15(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if location == 25:
        r.room25(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if location == 24:
        r.room24(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if location == 34:
        r.room34(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    

def rollInitiative(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    hero_roll = random.randint(1, 20)
    monster_roll = random.randint(1, 20)
    if hero_roll >= monster_roll:
        hero_attack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        monster_attack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);


def combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print "What would like to do?"
    print ""
    print "(A)ttack"
    print ""
    print "(S)pell book"
    print ""
    action = raw_input('>')
    if action in ['a', 'A']:
        heroAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used); 
    if action in ['s', 'S']:
        sb.spellBook(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        

def heroAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    attack_roll = random.randint(1, 20)
    if attack_roll >= encounter_monsterAC:
        print ""
        print "You hit!"
        print ""
        damage_die1 = random.randint(1,4)
        damage_die2 = random.randint(1,4)
        total_damage = (heroHD * damage_die1) + (heroHD * damage_die2)
        time.sleep(1)
        print "You do",total_damage,"points of damage."
        time.sleep(1)
        encounter_monsterHP = encounter_monsterHP - total_damage
        print ""
        print "The",encounter_monsterName,"has",encounter_monsterHP,"hit points remaining."
        check_monster_death(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        print ""
        print "You miss!"
        time.sleep(1)
        monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);


def monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    print ""
    print "A", encounter_monsterName,"attacks!"
    print ""
    time.sleep(1)
    attack_roll = random.randint(1, 20)
    if attack_roll >= heroAC:
        time.sleep(1)
        print "The",encounter_monsterName,"hits!"
        print ""
        damage_die1 = random.randint(1,4)
        damage_die2 = random.randint(1,4)
        total_damage = (encounter_monsterHD * damage_die1) + (encounter_monsterHD * damage_die2)
        time.sleep(2)
        print "The",encounter_monsterName,"does",total_damage,"points of damage!"
        print ""
        print "You have", heroHP,"points of health remaining."
        time.sleep(1)
        check_hero_death(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        print "The",encounter_monsterName,"misses!"
        print ""
        combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);


def check_monster_death(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if encounter_monsterHP <= 0:
        print ""
        print "The",encounter_monsterName,"has been killed!"
        time.sleep(1)
        get_new_monster(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    else:
        monsterAttack(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);

def check_hero_death(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if heroHP <= 0:
        print ""
        print "You have died!"
        print ""
        print "GAME OVER"
        time.sleep(2)
        sys.exit()
    else:
        combat_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
        
def get_new_monster(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used):
    if encounter_monsterName == 'kobold guard':
        encounter_monsterName = m2.monsterName
        encounter_monsterHP = m2.monsterHP
        encounter_monsterAC = m2.monsterAC
        encounter_monsterHD = m2.monsterHD
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if  encounter_monsterName == 'spider':
        encounter_monsterName = m3.monsterName
        encounter_monsterHP = m3.monsterHP
        encounter_monsterAC = m3.monsterAC
        encounter_monsterHD = m3.monsterHD
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    if encounter_monsterName == 'ogre':
        encounter_monsterName = m4.monsterName
        encounter_monsterHP = m4.monsterHP
        encounter_monsterAC = m4.monsterAC
        encounter_monsterHD = m4.monsterHD
        nav_menu(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, heroHP, heroAC, heroHD, heroSTR, heroDEX, heroCON, heroWIS, heroINT, heroCHA, heal_used, lightening_used, curse_used);
    
    
