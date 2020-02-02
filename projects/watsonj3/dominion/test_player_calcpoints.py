from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion


class TestPlayer(TestCase):

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


    def test_calcpoints(self):

        self.setUp()
        # add some cards to the player deck
        self.player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3 + [Dominion.Gardens()] * 2 + [Dominion.Cellar()] * 1
        # initialize tally variable with the return of calcpoints
        tally = self.player.calcpoints()
        # the expected tally should be 8
        self.assertEqual(8, tally)

