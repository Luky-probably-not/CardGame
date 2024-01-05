import random as rand

class Player:

    def __init__(self,mana,hp,deck):
        self.m = mana
        self.mmax = mana
        self.hpmax, self.hp = hp, hp
        self.deck = deck
        self.pioche = deck
        self.shield = 0
        self.strengh = 0
        self.resis = 0
        self.tstrengh = 0
        self.tresis = 0
        self.trash = []
        self.InitHand()
        self.gold = 100

    def __repr__(self):
        print(self.hand[0])
        print(self.hand[1])
        print(self.hand[2])
        print(self.pioche)
        return ""


    def InitHand(self):
        l = []
        i = 1
        while len(l) != 3 :
            a = rand.randint(0,len(self.pioche)-i)
            if l.count(a) == 0 :
                l.append(self.pioche[a])
                self.pioche.remove(self.pioche[a])
                i += 1
        self.hand = []
        for i in l:
            self.hand.append(i)
        

    def updateHand(self,index):
        if len(self.pioche) == 0:
            rand.shuffle(self.trash)
            self.pioche = self.trash
            self.trash = []
        self.trash.append(self.hand[index])
        self.hand[index] = self.pioche[0]
        self.pioche.remove(self.pioche[0])

    def endTurn(self):
        self.strengh -= self.tstrengh
        self.resis -= self.tresis
        self.tstrengh = 0
        self.tresis = 0
        for i in range(3):
            self.updateHand(i)

    def hunter(self,enemy):
        enemy.hp -= 2

    def mage(self):
        self.mmax += 1
    
    def barbarian(self,receivedamage):
        self.tstrengh += receivedamage
        
