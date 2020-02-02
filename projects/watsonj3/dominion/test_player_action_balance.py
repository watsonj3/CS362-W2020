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


    def test_action_balance(self):

        self.setUp()

        # there should be 10 cards in the player stack
        self.assertEqual(10, len(self.player.stack()))
        # re-initialize list with new cards, including an action card
        self.player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3 + [Dominion.Woodcutter()] * 1
        # initialize action_balance variable with the return of action_balance method
        action_balance = self.player.action_balance()
        # expected value is -3.68...
        self.assertEqual(-3.6842105263157894, action_balance)







