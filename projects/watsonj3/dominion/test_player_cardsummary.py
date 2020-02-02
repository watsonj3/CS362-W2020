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


    def test_cardsummary(self):

        self.setUp()
        # add a Festival card to the deck
        self.player.deck = [Dominion.Festival()]
        # initialize summary variable with the return of cardsummary().  It should be a dict
        summary = self.player.cardsummary()
        # should have 4 keys and values
        self.assertEqual(4, len(summary.keys()))
        self.assertEqual(4, len(summary.values()))
        # summary dict should have a Festival key with a value of 1
        self.assertEqual(1, summary.get('Festival'))
        # summary dict should have a VICTORY POINTS key with a value of 1
        self.assertEqual(1, summary.get('VICTORY POINTS'))
        # summary dict should have a Copper key with a value of 4
        self.assertEqual(4, summary.get('Copper'))
        # summary dict should have a Estate key with a value of 1
        self.assertEqual(1, summary.get('Estate'))



