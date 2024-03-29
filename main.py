from func.cards import *
from func.enemies import *
from func.player import * 
from func.display import *
from func.action import *
from func.start import *
from func.encounter import *
from func.shop import *
from func.map import *
import random as rand
import copy
p1, map = InitGame()
Smap = copy.deepcopy(map)
if p1.rank == "mage":
    p1.mage()
a = checkHp = True
level = 1

while a:
    i = map.node.info
    if type(i) == Enemy:
        while i.hp > 0 and checkHp:
            checkHp = Turn(p1,i)
        if checkHp == False:
            break
        p1.gold += rand.randint(15,25)
    elif type(i) == Shop:
        i = Encounter("Magasin",Shop()).init()
        time.sleep(1)
        i.interact(p1)
    round(p1)
    a = map.choiceMap()
    if not a:
        a = True
        map = Copy(Smap)
        Smap = copy.deepcopy(map)
        level += 1
        p1.hp += 5
        if p1.hp > p1.hpmax:
            p1.hp = p1.hpmax
        print("Difficulty increased, now level : " + str(level))
        time.sleep(2)

        
        
if checkHp == False:
    print("You lose")
else:
    print("Congratulations")
