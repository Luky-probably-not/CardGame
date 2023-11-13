import time
from func.display import *
import random

def Turn(player,enemy):
    time.sleep(1)
    player.shield = 0
    player.m = player.mmax
    player.strengh += player.tstrengh
    player.resis += player.tresis
    display(player,enemy)
    
    while enemy.hp > 0 and player.m != 0:
        playerAction(player,enemy)
        if enemy.hp <= 0:
            enemy.hp = 0
        
    player.endTurn()
    if enemy.hp > 0:
        enemy.shield = 0
        enemyAction(player,enemy)
        if player.hp <= 0:
            player.hp = 0
            display(player,enemy)
            return False
    return True
    

    


def enemyAction(player,enemy):
    if enemy.p[0] == "atk":
        if player.shield >= enemy.a + enemy.strengh:
            player.shield -= (enemy.a + enemy.strengh)
        else:
            player.hp -= ((enemy.a + enemy.strengh) - player.shield)
            if player.rank == "barbarian":
                player.barbarian(((enemy.a + enemy.strengh) - player.shield))
            player.shield = 0
    elif enemy.p[0] == "def":
        enemy.shield += enemy.d
    elif enemy.p[0] == "buff":
        enemy.strengh += enemy.buff
    elif enemy.p[0] == "heal":
        enemy.hp += enemy.d
        if enemy.hp > enemy.hpmax:
            enemy.hp = enemy.hpmax
    elif enemy.p[0] == "crit":
        if player.shield >= (enemy.a + enemy.strengh)*2:
            player.shield -= (enemy.a + enemy.strengh)*2
        else:
            player.hp -= ((enemy.a + enemy.strengh)*2 - player.shield)
    enemy.p.append(enemy.p[0])
    enemy.p.remove(enemy.p[0])
    display(player,enemy)
    


def playerAction(player, enemy):
    print("What card to play ?")
    move = input()
    while move != "1" and move != "2" and move != "3" and move != "q" and move != "Q":
        print("Bad input, try again (type between 1 and 3 or q if you want to pass your turn)")
        move = input()
    if move == "q" or move == "Q":
        player.m = 0
        display(player,enemy)
        return
    move = int(move)-1
    action(player, move, enemy)
    display(player,enemy)
    
    time.sleep(1)
    
def action(player, index, enemy):
    card = player.hand[index]
    if card.eff == "atk":
        if enemy.shield >= card.s + player.strengh:
            enemy.shield -= (card.s + player.strengh)
        else:
            enemy.hp -= (card.s + player.strengh)-enemy.shield
            enemy.shield = 0
        if enemy.hp < 0 :
            enemy.hp = 0
    elif card.eff == "def":
        player.shield += (card.s + player.resis)
    elif card.eff == "heal":
        player.hp += card.s
        if player.hp > player.hpmax:
            player.hp = player.hpmax
    elif card.eff == "buff":
        player.tstrengh += 1 
        player.strengh += 1   
        player.tresis += 1
        player.resis += 1
        player.m += 1
    if player.rank == "hunter":
        player.hunter(enemy)
        if enemy.hp <= 0:
            enemy.hp = 0
    player.updateHand(index)
    player.m -= 1

def round(player):
    player.strengh = 0
    player.resis = 0


    

    