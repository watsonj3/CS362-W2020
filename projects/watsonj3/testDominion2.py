# -*- coding: utf-8 -*-
"""
Created on Jan 16/2020

@author: Jason Watson
"""

from projects.watsonj3.dominion import Dominion
from projects.watsonj3 import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#introduce bug here: change '>' to '<'
if len(player_names) < 2:
    nV = 12
else:
    nV = 8


#number of curses and victory cards
#nV = testUtility.getNumVictoryCards(player_names)
nC = -10 + 10 * len(player_names)

#define box from testUtility package (refactored from original)
box = testUtility.getBoxes(nV)

#define supply_order from testUtility package (refactored from original
supply_order = testUtility.getSupplyOrder()

#Get 10 random cards
random10 = testUtility.getTenRandomCards(box)

#initialize supply cards
supply = testUtility.getSupply(box, random10, player_names, nV, nC, )


#initialize the trash
trash = []

#construct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)