import random as rand
from func.encounter import *
from func.enemies import *
class Node:

    def __init__(self,encounter,a,b,index):
        self.name = encounter.name
        self.type = encounter.info
        self.left = a
        self.right = b
        self.index = index
        self.position = 4

    def __repr__(self):
        return self.print()
    
    def print(self):
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
        if left == None and right != None:
            return self.name + "(" + right + ")"
        elif left == None and right != None:
            return self.name + "(" + left + ")"
        elif left == None and right == None:
            return self.name
        else:
            return self.name + "(" + left + "," + right + ")"

class Map:

    def __init__(self):
        self.mapVisuel = self.emptyMap()
        self.map = []

    def emptyMap(self):
        total = []
        for i in range(9):
            ligne = []
            for i in range(30):
                ligne.append(" ")
            total.append(ligne)
        return total

    
    def displayMap(self):
        for i in self.mapVisuel:
            line = ""
            for f in i:
                line += f + " "
            print(line)
        
    def fillMap(self,listeNode):
        if len(listeNode) == 1:
            return listeNode[0]
        a = listeNode[0]
        self.node = a
        if a.up != None:
            self.map.append(a.up)
        if a.down != None:
            self.map.append(a.down)
        self.node = a
    
    
    def insertNode(self,node):
        if node.name == "Magasin":
            node.position = 5
        if node.name == "Boss":
            node.position = 5
            self.map[5][10] = node.name[0]
            return
        self.map[node.position][node.index*2] = node.name[0]
        if node.name == "Magasin":
            self.map[node.position-1][node.index*2-1] = "\\"
            self.map[node.position-2][node.index*2-1] = "\\"
            self.map[node.position+1][node.index*2-1] = "/"
        if node.up != None and node.dowb != None:
            self.map[node.position+1][node.index*2+1] = "\\"
            node.down.position = node.position+1
            self.map[node.position-1][node.index*2+1] = "/"
            node.up.position = node.position-1
        elif node.up == None or node.down == None:
            self.map[node.position][node.index*2+1] = "-"
            node.up.position = node.position

"""
print("map1")
print("             /-------- S --------- H --------\\")
print("            /                                 \\")
print("           /                                   \\")
print("Z -------- S             / ------- H ---------- \\")
print("           \            /                        M -------- B")
print("            \--------  Z                        /")
print("                        \                      /")
print("                         \ ------- H -------- /")

mobs = InitMobs()
zombie = Encounter("Zombie",mobs[0])
squelette = Encounter("Squelette",mobs[1])
harpie = Encounter("Harpie",mobs[2])
boss = Encounter("Boss",mobs[3])
magasin = Encounter("Magasin","info")
I = Node(boss,None,None,5)       
H = Node(magasin,I,None,4)
G = Node(harpie,H,None,3)
F = Node(harpie,H,None,3)
E = Node(harpie,H,None,3)
D = Node(zombie,F,G,2)
C = Node(squelette,E,None,2)
B = Node(squelette,C,D,1)
A = Node(zombie,B,None,0)
map1 = [A,B,C,D,E,F,G,H,I]






map = Map()
map.fillMap(map1)


print(map.node)
print(map.map[0].up)
print(map.node.up.down)
"""