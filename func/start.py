from func.cards import * 
from func.enemies import *
from func.player import *
from func.map import *
import copy

def start():
    deck = InitCard()
    p1 = Player(3,30,deck)
    print("What class would you like to play ?")
    print("     -hunter     (h)  : deal 2 damage every card played")
    print("     -mage       (m)  : gain +1 mana max")
    print("     -barbarian  (b)  : gain temporal strengh when you receive damage")
    p1.rank = input()
    while p1.rank != "h" and p1.rank != "m" and p1.rank != "b":
        print("Bad input, try again")
        p1.rank = input()
    if p1.rank == "h":
        p1.rank = "hunter"
    elif p1.rank == "m":
        p1.rank = "mage"
    elif p1.rank == "b":
        p1.rank = "barbarian"
    return p1, InitMobs()

def InitGame():
    p1,mobs = start()
    #Possible Encounter
    zombie = Encounter("Zombie",mobs[0]).init()
    squelette = Encounter("Squelette",mobs[1]).init()
    harpie = Encounter("Harpie",mobs[2]).init()
    boss = Encounter("Boss",mobs[3]).init()
    magasin = Encounter("Magasin",Shop()).init()
    I = Node(copy.deepcopy(boss),None,None,5)       
    H = Node(copy.deepcopy(magasin),I,None,4)
    G = Node(copy.deepcopy(harpie),H,None,3)
    F = Node(copy.deepcopy(harpie),H,None,3)
    E = Node(copy.deepcopy(harpie),H,None,3)
    D = Node(copy.deepcopy(zombie),F,G,2)
    C = Node(copy.deepcopy(squelette),E,None,2)
    B = Node(copy.deepcopy(squelette),C,D,1)
    A = Node(copy.deepcopy(zombie),B,None,0)
    map = Map(A,I)
    return p1, map
