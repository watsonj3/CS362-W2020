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


    def test_draw(self):

        self.setUp()
        # add a list of cards to card variable
        card = [Dominion.Woodcutter()] + [Dominion.Copper()] + [Dominion.Cellar()]
        # add cards to discard list
        self.player.discard = card
        # initialize empty player deck
        self.player.deck = []
        # call draw() method
        self.player.draw()

        # length of deck should be 2
        self.assertEqual(2, len(self.player.deck))
        # discard list should be empty
        self.assertEqual(0, len(self.player.discard))



