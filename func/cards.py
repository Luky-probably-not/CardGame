import random as rand

class Card:

    def __init__(self,nom,effet,stat):
        self.n = nom
        self.eff = effet
        self.s = stat

    def __repr__(self):
        return "(" + self.n + ", " + self.eff + ", " + str(self.s) + ")"

def InitCard():
    frappe = Card("frappe","atk",5)
    defense = Card("defense", "def", 5)
    soin = Card("soin", "heal", 2)
    boost = Card("magic", "buff",1)
    l = [frappe,soin,boost]
    for i in range(2):
        l.append(frappe)
        l.append(defense)
    rand.shuffle(l)
    return l
"""
list = ["🗡️", "🛡️", "⚔️", "❤️‍🩹", "🔥"]
"""