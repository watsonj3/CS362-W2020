from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion

class TestCard(TestCase):

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

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        #instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # verify that the class variables have the expected values
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass

