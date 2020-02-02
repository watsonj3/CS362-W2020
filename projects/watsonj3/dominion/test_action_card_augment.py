from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion

class TestAction_card(TestCase):

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

    def test_augment(self):

        self.setUp()

        self.player.actions = 1
        self.player.buys = 1
        self.player.purse = 0

        Dominion.Woodcutter().augment(self.player)

        self.assertEqual(1, self.player.actions)
        self.assertEqual(2, self.player.buys)
        self.assertEqual(2, self.player.purse)
