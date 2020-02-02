from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion



class TestAction_card(TestCase):

    def setUp(self):
        # data setup
        self.players = testUtility.getPlayers()
        self.nV = testUtility.getNumVictoryCards(self.players)
        self.nC = testUtility.getNumCurseCards(self.players)
        self.box = testUtility.getBoxes(self.nV)
        self.supply_order = testUtility.getSupplyOrder()

        self.supply = testUtility.getSupply(self.box, self.players, self.nV, self.nC)
        self.trash = []




    def test_init(self):
        self.fail()

    def test_use(self):
        self.fail()

    def test_augment(self):
        self.fail()

    def test_play(self):
        self.fail()
