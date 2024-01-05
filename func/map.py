from func.encounter import *
from func.enemies import *
from func.shop import *
import random as rand
import copy
import time

class Node:

    def __init__(self,node,left,right,index):
        self.name = node.name
        self.info = node
        self.left = left
        self.right = right

    def __repr__(self):
        return self.print()

    def print(self):
        left,right = self.printNode()
        if left == None and right != None:
            return self.name + "(" + right + ")"
        elif left != None and right == None:
            return self.name + "(" + left + ")"
        elif left == None and right == None:
            return self.name
        else:
            return self.name + "(" + left + "," + right + ")"
        
    def printNode(self):
        if self.left == None:
            left = None
        elif type(self.left) == Node:
            left = self.left.print()
        else:
            left = self.left
        if self.right == None:
            right = None
        elif type(self.right) == Node:
            right = self.right.print()
        else :
            right = self.right
        return left,right
    
    def buff(self):
        if self.left != None:
            self.left.buff()
        if self.right != None:
            self.right.buff()
        if type(self.info) == Enemy:
            self.info.hpmax += 5
            self.info.hp = self.info.hpmax
            self.info.a += 2
        return self
        
class Map:

    def __init__(self,nodeS,nodeE):
        self.start = self.node = nodeS
        self.end = nodeE
   
    def print(self):
        if self.node == None:
            return
        left = self.node.left
        right = self.node.right
        if left != None:
            left = left.name + " (left)"
        if right != None:
            right = right.name + " (right)"
        if left == None and right == None:
            return 
        elif left == None:
            print(right)
        elif right == None:
            print(left)       
        else:
            print(left + " or " + right)
    
    def choiceMap(self):
        if self.node == None or (self.node.left == None and self.node.right == None):
            return False
        print("\033c")
        self.print()   
        print("Where would you like to go ?")
        choice = input()
        while ((choice == "left" or choice == "LEFT") and self.node.left == None) or ((choice == "right" or choice == "RIGHT") and self.node.right == None) or (choice != "left" and choice != "LEFT" and choice != "right" and choice != "RIGHT"):
            print("Bad input")
            self.print()
            choice = input()
        if choice == "left" or choice == "LEFT":
            self.node = self.node.left
            return True
        elif "right" == choice or choice == "RIGHT":
            self.node = self.node.right
            return True

def Copy(Smap):
    map = copy.deepcopy(Smap)
    map.node = Smap.start.buff()
    return map
        

"""
mobs = InitMobs()
zombie = Encounter("Zombie",mobs[0]).init()
squelette = Encounter("Squelette",mobs[1]).init()
harpie = Encounter("Harpie",mobs[2]).init()
boss = Encounter("Boss",mobs[3]).init()
magasin = Encounter("Magasin",Shop()).init()
I = Node(boss,None,None,5)       
H = Node(magasin,I,None,4)
G = Node(harpie,H,None,3)
F = Node(harpie,H,None,3)
E = Node(harpie,H,None,3)
D = Node(zombie,F,G,2)
C = Node(squelette,E,None,2)
B = Node(squelette,C,D,1)
A = Node(zombie,B,None,0)
map = Map(A,I)
a = map.choiceMap()
while a:
    a = map.choiceMap()
    
print(A)
"""