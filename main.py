import game_functions as gf
from hero import Hero
from monster import Monster
from artwork import Artwork


import os
import random

hp = random.randint(12, 16)
ac = random.randint(12, 14)
hd = 2
STR = random.randint(3, 18)
DEX = random.randint(3, 18)
CON = random.randint(3, 18)
WIS = random.randint(3, 18)
INT = random.randint(3, 18)
CHA = random.randint(3, 18)

hero = Hero(hp, ac, hd, STR, DEX, CON, WIS, INT, CHA);

m1 = Monster('kobold guard', 12, 10, 1)


encounter_monsterName = m1.monsterName
encounter_monsterAC = m1.monsterAC
encounter_monsterHP = m1.monsterHP
encounter_monsterHD = m1.monsterHD


location = 5

rm5_visited = 0
rm15_visited = 0
rm25_visited = 0
rm24_visited = 0
rm34_visited = 0

heal_used = 0
lightening_used = 0
curse_used = 0

os.system('cls' if os.name == 'nt' else 'clear')
art = Artwork();
art.banner();
gf.room_router(location, rm5_visited, rm15_visited, rm25_visited, rm24_visited, rm34_visited, encounter_monsterName, encounter_monsterHP, encounter_monsterAC, encounter_monsterHD, hero.heroHP, hero.heroAC, hero.heroHD, hero.heroSTR, hero.heroDEX, hero.heroCON, hero.heroWIS, hero.heroINT, hero.heroCHA, heal_used, lightening_used, curse_used);
