from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion
import random
from collections import defaultdict


class TestGameover(TestCase):

    def setUp(self):

        #data setup

        self.players = testUtility.getPlayers()
        self.nV = testUtility.getNumVictoryCards(self.players)
        self.nC = testUtility.getNumCurseCards(self.players)
        self.box = testUtility.getBoxes(self.nV)
        self.supply_order = testUtility.getSupplyOrder()

        self.supply = testUtility.getSupply(self.box, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')


    def test_gameover(self):

        self.setUp()

        # initialize isGameOver with the default supply
        isGameOver = Dominion.gameover(self.supply)
        # should return an expected False
        self.assertEqual(False, isGameOver)

        # change the number of Province cards in the supply to 0
        self.supply["Province"] = [Dominion.Province()] * 0
        # re-initialize isGameOver by calling gameover with updated supply list
        isGameOver = Dominion.gameover(self.supply)
        # should return an expected True
        self.assertEqual(True, isGameOver)






