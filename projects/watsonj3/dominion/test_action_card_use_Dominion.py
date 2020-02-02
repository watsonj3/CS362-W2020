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


    def test_use(self):

        self.setUp()

        # initialize card with Woodcutter action card
        card = Dominion.Woodcutter()
        # add card to players hand
        self.player.hand.append(card)
        # assert length of player's hand.  It should have 6 cards
        self.assertEqual(len(self.player.hand), 6)
        # call use function
        card.use(self.player, self.trash)

        # determine that the played list has 1 card, and the hand list has 5
        self.assertEqual(len(self.player.played), 1)
        self.assertEqual(len(self.player.hand), 5)
